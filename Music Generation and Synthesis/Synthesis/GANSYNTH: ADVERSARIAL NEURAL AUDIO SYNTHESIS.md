#2019 [GANSYNTH: ADVERSARIAL NEURAL AUDIO SYNTHESIS](https://arxiv.org/abs/1902.08710)
Author: Engel, Jesse; Agrawal, Kumar Krishna; Chen, Shuo; Gulrajani, Ishaan; Donahue, Chris; Roberts, Adam
>Abstract: Efficient audio synthesis is an inherently difficult machine learning task, as human perception is sensitive to both global structure and fine-scale waveform coherence. Autoregressive models, such as WaveNet, model local structure but have slow iterative sampling and lack global latent structure. In contrast, Generative Adversarial Networks (GANs) have global latent conditioning and efficient parallel sampling, but struggle to generate locally-coherent audio waveforms. Herein, we demonstrate that GANs can in fact generate high-fidelity and locally-coherent audio by modeling log magnitudes and instantaneous frequencies with sufficient frequency resolution in the spectral domain. Through extensive empirical investigations on the NSynth dataset, we demonstrate that GANs are able to outperform strong WaveNet baselines on automated and human evaluation metrics, and efficiently generate audio several orders of magnitude faster than their autoregressive counterparts.

Data Set: [The NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth)

Source Code: [Source Code](https://github.com/tensorflow/magenta/tree/master/magenta/models/gansynth)

Demo: [Demo](https://colab.research.google.com/notebooks/magenta/gansynth/gansynth_demo.ipynb), [Demo](https://storage.googleapis.com/magentadata/papers/gansynth/index.html)

