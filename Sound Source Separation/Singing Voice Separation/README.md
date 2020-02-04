#  [WAVE-U-NET: A MULTI-SCALE NEURAL NETWORK FOR END-TO-END AUDIO SOURCE SEPARATION](https://arxiv.org/abs/1806.03185)
**Author**: Stoller, Daniel; Ewert, Sebastian; Dixon, Simon

**Year**: 2018
>**Abstract**: Models for audio source separation usually operate on the magnitude spectrum, which ignores phase information and makes separation performance dependant on hyperparameters for the spectral front-end. Therefore, we investigate end-to-end source separation in the time-domain, which allows modelling phase information and avoids ﬁxed spectral transformations. Due to high sampling rates for audio, employing a long temporal input context on the sample level is difﬁcult, but required for high quality separation results because of long-range temporal correlations. In this context, we propose the Wave-U-Net, an adaptation of the U-Net to the one-dimensional time domain, which repeatedly resamples feature maps to compute and combine features at different time scales. We introduce further architectural improvements, including an output layer that enforces source additivity, an upsampling technique and a context-aware prediction framework to reduce output artifacts. Experiments for singing voice separation indicate that our architecture yields a performance comparable to a stateof-the-art spectrogram-based U-Net architecture, given the same data. Finally, we reveal a problem with outliers in the currently used SDR evaluation metrics and suggest reporting rank-based statistics to alleviate this problem.

**Data Set**: [MUSDB](https://sigsep.github.io/datasets/musdb.html), [CCMixter database](http://dig.ccmixter.org/)

**Source Code**: [Source Code](https://github.com/f90/Wave-U-Net)

**Demo**: Not availabe

#  [Raw Multi-Channel Audio Source Separation using Multi-Resolution Convolutional Auto-Encoders](http://arxiv.org/abs/1803.00702)
**Author**: Grais, Emad M.; Ward, Dominic; Plumbley, Mark D.

**Year**: 2018
>**Abstract**: Supervised multi-channel audio source separation requires extracting useful spectral, temporal, and spatial features from the mixed signals. The success of many existing systems is therefore largely dependent on the choice of features used for training. In this work, we introduce a novel multi-channel, multiresolution convolutional auto-encoder neural network that works on raw time-domain signals to determine appropriate multiresolution features for separating the singing-voice from stereo music. Our experimental results show that the proposed method can achieve multi-channel audio source separation without the need for hand-crafted features or any pre- or post-processing.

**Data Set**: [SiSEC-2016-MUS-task dataset](https://sisec.inria.fr/sisec-2016/)

**Source Code**: [Source Code](https://cvssp.github.io/maruss-website/publications/Grais_2018.html)

**Demo**: Not availabe

