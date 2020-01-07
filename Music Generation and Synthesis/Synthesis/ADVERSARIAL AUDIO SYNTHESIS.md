#2019 [ADVERSARIAL AUDIO SYNTHESIS](https://arxiv.org/abs/1802.04208)
Author: Donahue, Chris; McAuley, Julian; Puckette, Miller
>Abstract: Audio signals are sampled at high temporal resolutions, and learning to synthesize audio requires capturing structure across a range of timescales. Generative adversarial networks (GANs) have seen wide success at generating images that are both locally and globally coherent, but they have seen little application to audio generation. In this paper we introduce WaveGAN, a ﬁrst attempt at applying GANs to unsupervised synthesis of raw-waveform audio. WaveGAN is capable of synthesizing one second slices of audio waveforms with global coherence, suitable for sound effect generation. Our experiments demonstrate that—without labels—WaveGAN learns to produce intelligible words when trained on a smallvocabulary speech dataset, and can also synthesize audio from other domains such as drums, bird vocalizations, and piano. We compare WaveGAN to a method which applies GANs designed for image generation on image-like audio feature representations, ﬁnding both approaches to be promising.

Data Set: [Speech Commands Dataset](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html), [Peter Boesman. Bird recordings.](https://www.xeno-canto.org/contributor/OOECIWCSWV)

Source Code: [Source Code](https://github.com/chrisdohue/wavegan)

Demo: [Demo](https://chrisdohue.com/wavegan_examples/), [Demo](https://chrisdohue.com/wavegan/)

