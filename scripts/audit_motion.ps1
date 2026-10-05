param(
    [Parameter(Mandatory = $true)]
    [string]$PptxPath,
    [string]$JsonPath
)

$ErrorActionPreference = 'Stop'
$msoMedia = 16
$app = $null
$presentation = $null

function Get-SafeValue {
    param([scriptblock]$Action, $Default = $null)
    try { & $Action } catch { $Default }
}

try {
    $resolved = (Resolve-Path -LiteralPath $PptxPath).Path
    $app = New-Object -ComObject PowerPoint.Application
    $presentation = $app.Presentations.Open($resolved, $true, $false, $false)

    $slides = foreach ($slide in @($presentation.Slides)) {
        $media = @()
        foreach ($shape in @($slide.Shapes)) {
            if ((Get-SafeValue { [int]$shape.Type } -1) -eq $msoMedia) {
                $media += [ordered]@{
                    name = Get-SafeValue { [string]$shape.Name } ''
                    type = 'media'
                    media_length_s = Get-SafeValue { [math]::Round(([double]$shape.MediaFormat.Length / 1000), 3) } $null
                    play_on_entry = Get-SafeValue { [bool]$shape.AnimationSettings.PlaySettings.PlayOnEntry } $null
                    loop_until_stopped = Get-SafeValue { [bool]$shape.AnimationSettings.PlaySettings.LoopUntilStopped } $null
                }
            }
        }

        $effects = @()
        $sequence = $slide.TimeLine.MainSequence
        for ($i = 1; $i -le (Get-SafeValue { [int]$sequence.Count } 0); $i++) {
            $effect = $sequence.Item($i)
            $effects += [ordered]@{
                index = $i
                effect_type = Get-SafeValue { [int]$effect.EffectType } $null
                shape_name = Get-SafeValue { [string]$effect.Shape.Name } ''
                trigger_type = Get-SafeValue { [int]$effect.Timing.TriggerType } $null
                duration_s = Get-SafeValue { [math]::Round([double]$effect.Timing.Duration, 3) } $null
                delay_s = Get-SafeValue { [math]::Round([double]$effect.Timing.TriggerDelayTime, 3) } $null
            }
        }

        [ordered]@{
            page = [int]$slide.SlideIndex
            transition = [ordered]@{
                entry_effect = Get-SafeValue { [int]$slide.SlideShowTransition.EntryEffect } $null
                speed = Get-SafeValue { [int]$slide.SlideShowTransition.Speed } $null
                advance_on_click = Get-SafeValue { [bool]$slide.SlideShowTransition.AdvanceOnClick } $null
                advance_on_time = Get-SafeValue { [bool]$slide.SlideShowTransition.AdvanceOnTime } $null
            }
            media = $media
            main_sequence = $effects
            interactive_sequence_count = Get-SafeValue { [int]$slide.TimeLine.InteractiveSequences.Count } 0
        }
    }

    $issues = @()
    foreach ($slide in $slides) {
        $mediaFirst = $slide.media.Count -eq 0 -or (
            $slide.main_sequence.Count -gt 0 -and
            $slide.main_sequence[0].effect_type -eq 83 -and
            $slide.main_sequence[0].trigger_type -eq 2 -and
            $slide.main_sequence[0].delay_s -eq 0
        )
        if (-not $mediaFirst) { $issues += "slide-$($slide.page): media effect is not first/WithPrevious/t=0" }
        if ($slide.transition.advance_on_time -eq $true) { $issues += "slide-$($slide.page): timed advance enabled" }
    }

    $result = [ordered]@{
        pptx = $resolved
        office_version = Get-SafeValue { [string]$app.Version } ''
        slide_count = $slides.Count
        slides = $slides
        status = if ($issues.Count) { 'review_required' } else { 'structure_ok' }
        issues = $issues
    }
    $json = $result | ConvertTo-Json -Depth 8
    if ($JsonPath) {
        $json | Set-Content -LiteralPath $JsonPath -Encoding utf8
    }
    $json
}
finally {
    if ($presentation) {
        try { $presentation.Close() } catch {}
        [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($presentation)
    }
    if ($app) {
        try { $app.Quit() } catch {}
        [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

