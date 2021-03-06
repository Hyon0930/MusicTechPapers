#  [GANSYNTH: ADVERSARIAL NEURAL AUDIO SYNTHESIS](https://arxiv.org/abs/1902.08710)
**Author**: Engel, Jesse; Agrawal, Kumar Krishna; Chen, Shuo; Gulrajani, Ishaan; Donahue, Chris; Roberts, Adam

**Year**: 2019
>**Abstract**: Efficient audio synthesis is an inherently difficult machine learning task, as human perception is sensitive to both global structure and fine-scale waveform coherence. Autoregressive models, such as WaveNet, model local structure but have slow iterative sampling and lack global latent structure. In contrast, Generative Adversarial Networks (GANs) have global latent conditioning and efficient parallel sampling, but struggle to generate locally-coherent audio waveforms. Herein, we demonstrate that GANs can in fact generate high-fidelity and locally-coherent audio by modeling log magnitudes and instantaneous frequencies with sufficient frequency resolution in the spectral domain. Through extensive empirical investigations on the NSynth dataset, we demonstrate that GANs are able to outperform strong WaveNet baselines on automated and human evaluation metrics, and efficiently generate audio several orders of magnitude faster than their autoregressive counterparts.

**Data Set**: [The NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth)

**Source Code**: [Source Code](https://github.com/tensorflow/magenta/tree/master/magenta/models/gansynth)

**Demo**: [Demo](https://colab.research.google.com/notebooks/magenta/gansynth/gansynth_demo.ipynb), [Demo](https://storage.googleapis.com/magentadata/papers/gansynth/index.html)

#  [Adversarial Generation of Time-Frequency Features with application in audio synthesis](https://arxiv.org/abs/1902.04072)
**Author**: Marafioti, Andrés; Holighaus, Nicki; Perraudin, Nathanaël; Majdak, Piotr

**Year**: 2019
>**Abstract**: Time-frequency (TF) representations provide powerful and intuitive features for the analysis of time series such as audio. But still, generative modeling of audio in the TF domain is a subtle matter. Consequently, neural audio synthesis widely relies on directly modeling the waveform and previous attempts at unconditionally synthesizing audio from neurally generated invertible TF features still struggle to produce audio at satisfying quality. In this article, focusing on the short-time Fourier transform, we discuss the challenges that arise in audio synthesis based on generated invertible TF features and how to overcome them. We demonstrate the potential of deliberate generative TF modeling by training a generative adversarial network (GAN) on short-time Fourier features. We show that by applying our guidelines, our TF-based network was able to outperform a state-of-the-art GAN generating waveforms directly, despite the similar architecture in the two networks.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [ADVERSARIAL AUDIO SYNTHESIS](https://arxiv.org/abs/1802.04208)
**Author**: Donahue, Chris; McAuley, Julian; Puckette, Miller

**Year**: 2019
>**Abstract**: Audio signals are sampled at high temporal resolutions, and learning to synthesize audio requires capturing structure across a range of timescales. Generative adversarial networks (GANs) have seen wide success at generating images that are both locally and globally coherent, but they have seen little application to audio generation. In this paper we introduce WaveGAN, a ﬁrst attempt at applying GANs to unsupervised synthesis of raw-waveform audio. WaveGAN is capable of synthesizing one second slices of audio waveforms with global coherence, suitable for sound effect generation. Our experiments demonstrate that—without labels—WaveGAN learns to produce intelligible words when trained on a smallvocabulary speech dataset, and can also synthesize audio from other domains such as drums, bird vocalizations, and piano. We compare WaveGAN to a method which applies GANs designed for image generation on image-like audio feature representations, ﬁnding both approaches to be promising.

**Data Set**: [Speech Commands Dataset](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html), [Peter Boesman. Bird recordings.](https://www.xeno-canto.org/contributor/OOECIWCSWV)

**Source Code**: [Source Code](https://github.com/chrisdohue/wavegan)

**Demo**: [Demo](https://chrisdohue.com/wavegan_examples/), [Demo](https://chrisdohue.com/wavegan/)

