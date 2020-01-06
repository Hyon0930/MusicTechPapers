#2015 [Deep clustering: Discriminative embeddings for segmentation and separation](http://arxiv.org/abs/1508.04306)
Author: Hershey, John R.; Chen, Zhuo; Roux, Jonathan Le; Watanabe, Shinji
>Abstract: We address the problem of acoustic source separation in a deep learning framework we call “deep clustering”. Rather than directly estimating signals or masking functions, we train a deep network to produce spectrogram embeddings that are discriminative for partition labels given in training data. Previous deep network approaches provide great advantages in terms of learning power and speed, but previously it has been unclear how to use them to separate signals in a classindependent way. In contrast, spectral clustering approaches are ﬂexible with respect to the classes and number of items to be segmented, but it has been unclear how to leverage the learning power and speed of deep networks. To obtain the best of both worlds, we use an objective function that to train embeddings that yield a low-rank approximation to an ideal pairwise afﬁnity matrix, in a classindependent way. This avoids the high cost of spectral factorization and instead produces compact clusters that are amenable to simple clustering methods. The segmentations are therefore implicitly encoded in the embeddings, and can be ”decoded” by clustering. Preliminary experiments show that the proposed method can separate speech: when trained on spectrogram features containing mixtures of two speakers, and tested on mixtures of a held-out set of speakers, it can infer masking functions that improve signal quality by around 6dB. We show that the model can generalize to three-speaker mixtures despite training only on twospeaker mixtures. The framework can be used without class labels, and therefore has the potential to be trained on a diverse set of sound types, and to generalize to novel sources. We hope that future work will lead to segmentation of arbitrary sounds, with extensions to microphone array methods as well as image segmentation and other domains.

Data Set: [CSR-I (WSJ0) Complete](https://catalog.ldc.upenn.edu/LDC93S6A)

Source Code: [Source Code](https://sourceforge.net/projects/currennt/)

Demo: Not availabe
