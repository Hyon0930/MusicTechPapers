#  [A Partitioned Autoencoder for Audio De-Noising](http://ee.cooper.edu/~keene/assets/lusterman_thesis.pdf)
**Author**: Lusterman, Ethan

**Year**: 2016
>**Abstract**: In this thesis, we introduce a modified partitioned autoencoder for de-noising audio without access to clean data for training. Traditional linear timeinvariant (LTI) systems such as the Wiener filter rely on power spectral density (PSD) estimates of desired signals and noise signals, which require some knowledge of the ground truth signals. One nonlinear approach in this area includes the use of de-noising autoencoders, which are one form of artificial neural networks (ANN). The nonlinearity of neural networks allow for more complex models to be made than LTI models. However, since de-noising autoencoders also require access to clean data and knowledge of the noise corruption process, we build on existing literature for a semi-supervised partitioned autoencoder that can perform de-noising without the clean signals during training. We compare existing semi-supervised de-noising systems as well as canonical supervised de-noising autoencoders. We show that for moderate levels of noise, our autoencoder outperforms existing schemes.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Speech Enhancement Based on Deep Denoising Autoencoder](https://www.isca-speech.org/archive/archive_papers/interspeech_2013/i13_0436.pdf)
**Author**: Lu, Xugang; Tsao, Yu; Matsuda, Shigeki; Hori, Chiori

**Year**: 2013
>**Abstract**: We previously have applied deep autoencoder (DAE) for noise reduction and speech enhancement. However, the DAE was trained using only clean speech. In this study, by using noisyclean training pairs, we further introduce a denoising process in learning the DAE. In training the DAE, we still adopt greedy layer-wised pretraining plus ﬁne tuning strategy. In pretraining, each layer is trained as a one-hidden-layer neural autoencoder (AE) using noisy-clean speech pairs as input and output (or transformed noisy-clean speech pairs by preceding AEs). Fine tuning was done by stacking all AEs with pretrained parameters for initialization. The trained DAE is used as a ﬁlter for speech estimation when noisy speech is given. Speech enhancement experiments were done to examine the performance of the trained denoising DAE. Noise reduction, speech distortion, and perceptual evaluation of speech quality (PESQ) criteria are used in the performance evaluations. Experimental results show that adding depth of the DAE consistently increase the performance when a large training data set is given. In addition, compared with a minimum mean square error based speech enhancement algorithm, our proposed denoising DAE provided superior performance on the three objective evaluations.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

