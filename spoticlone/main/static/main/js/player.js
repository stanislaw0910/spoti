let trackUrl = '{{ track_url|safe }}'

var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    scrollParent: true
});

wavesurfer.load(trackUrl)
function startRecording() {
  wavesurfer.play()
}
function pauseRecording() {
  wavesurfer.pause()
}
function stopRecording() {
  wavesurfer.stop()
}