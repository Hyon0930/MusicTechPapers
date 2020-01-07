#2019 [Sparse Pursuit and Dictionary Learning for Blind Source Separation in Polyphonic Music Recordings](http://arxiv.org/abs/1806.00273)
Author: Schulze, Sören; King, Emily J.
>Abstract: We propose a novel method for the blind separation of single-channel audio signals produced by the mixed sounds of musical instruments. While the approach of applying non-negative matrix factorization (NMF) has been studied in many papers, it does not make use of the pitch-invariance that the sounds of many instruments exhibit. This limitation can be overcome by using tensor factorization, in which context the use of log-frequency spectrograms was initiated, but this still requires the specific tuning of the instruments to be hard-coded into the algorithm. We develop a general-purpose sparse pursuit method that matches a discrete spectrum with given shifted continuous patterns. We first use it in order to transform our audio signal into a log-frequency spectrogram that shares properties with the mel spectrogram but is applicable to a wider frequency range. Then, we use the same algorithm to identify patterns from instrument sounds in the spectrogram. The relative amplitudes of the harmonics are saved in a dictionary, which is trained via a modified version of Adam. For a realistic monaural piece with acoustic recorder and violin, we achieve qualitatively good separation with a signal-to-distortion ratio (SDR) of 13.7 dB, a signal-to-interference ratio (SIR) of 28.1 dB, and a signal-to-artifacts ratio (SAR) of 13.9 dB, averaged over the instruments.

Data Set: Not availabe

Source Code: [Source Code](https://github.com/rgcda/Musisep)

Demo: [Demo](https://www.math.colostate.edu/~king/software.html#Musisep)

