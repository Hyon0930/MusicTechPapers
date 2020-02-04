#  [Improving music source separation based on deep neural networks through data augmentation and network blending](http://ieeexplore.ieee.org/document/7952158/)
**Author**: Uhlich, Stefan; Porcu, Marcello; Giron, Franck; Enenkl, Michael; Kemp, Thomas; Takahashi, Naoya; Mitsufuji, Yuki

**Year**: 2017
>**Abstract**: This paper deals with the separation of music into individual instrument tracks which is known to be a challenging problem. We describe two different deep neural network architectures for this task, a feed-forward and a recurrent one, and show that each of them yields themselves state-of-the art results on the SiSEC DSD100 dataset. For the recurrent network, we use data augmentation during training and show that even simple separation networks are prone to overﬁtting if no data augmentation is used. Furthermore, we propose a blending of both neural network systems where we linearly combine their raw outputs and then perform a multi-channel Wiener ﬁlter post-processing. This blending scheme yields the best results that have been reported to-date on the SiSEC DSD100 dataset.

**Data Set**: [DSD100](https://sigsep.github.io/datasets/dsd100.html)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Deep convolutional neural networks for predominant instrument recognition in polyphonic music](http://arxiv.org/abs/1605.09507)
**Author**: Han, Yoonchang; Kim, Jaehun; Lee, Kyogu

**Year**: 2017
>**Abstract**: Identifying musical instruments in polyphonic music recordings is a challenging but important problem in the ﬁeld of music information retrieval. It enables music search by instrument, helps recognize musical genres, or can make music transcription easier and more accurate. In this paper, we present a convolutional neural network framework for predominant instrument recognition in real-world polyphonic music. We train our network from ﬁxed-length music excerpts with a single-labeled predominant instrument and estimate an arbitrary number of predominant instruments from an audio signal with a variable length. To obtain the audio-excerpt-wise result, we aggregate multiple outputs from sliding windows over the test audio. In doing so, we investigated two different aggregation methods: one takes the average for each instrument and the other takes the instrument-wise sum followed by normalization. In addition, we conducted extensive experiments on several important factors that affect the performance, including analysis window size, identiﬁcation threshold, and activation functions for neural networks to ﬁnd the optimal set of parameters. Using a dataset of 10k audio excerpts from 11 instruments for evaluation, we found that convolutional neural networks are more robust than conventional methods that exploit spectral features and source separation with support vector machines. Experimental results showed that the proposed convolutional network architecture obtained an F1 measure of 0.602 for micro and 0.503 for macro, respectively, achieving 19.6% and 16.4% in performance improvement compared with other state-of-the-art algorithms.

**Data Set**: [RWC Music Database](https://staff.aist.go.jp/m.goto/RWC-MDB/)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Monoaural Audio Source Separation Using Deep Convolutional Neural Networks](http://link.springer.com/10.1007/978-3-319-53547-0_25)
**Author**: Chandna, Pritish; Miron, Marius; Janer, Jordi; Gómez, Emilia

**Year**: 2017
>**Abstract**: In this paper we introduce a low-latency monaural source separation framework using a Convolutional Neural Network (CNN). We use a CNN to estimate time-frequency soft masks which are applied for source separation. We evaluate the performance of the neural network on a database comprising of musical mixtures of three instruments: voice, drums, bass as well as other instruments which vary from song to song. The proposed architecture is compared to a Multilayer Perceptron (MLP), achieving on-par results and a signiﬁcant improvement in processing time. The algorithm was submitted to source separation evaluation campaigns to test eﬃciency, and achieved competitive results.

**Data Set**: [DSD100](https://sigsep.github.io/datasets/dsd100.html)

**Source Code**: [Source Code](https://github.com/MTG/DeepConvSep)

**Demo**: [Demo](https://www.youtube.com/watch?v=71WwHyDfE)

#  [Single Channel Audio Source Separation using Convolutional Denoising Autoencoders](http://arxiv.org/abs/1703.08019)
**Author**: Grais, Emad M.; Plumbley, Mark D.

**Year**: 2017
>**Abstract**: Deep learning techniques have been used recently to tackle the audio source separation problem. In this work, we propose to use deep fully convolutional denoising autoencoders (CDAEs) for monaural audio source separation. We use as many CDAEs as the number of sources to be separated from the mixed signal. Each CDAE is trained to separate one source and treats the other sources as background noise. The main idea is to allow each CDAE to learn suitable spectral-temporal ﬁlters and features to its corresponding source. Our experimental results show that CDAEs perform source separation slightly better than the deep feedforward neural networks (FNNs) even with fewer parameters than FNNs.

**Data Set**: [SiSEC-2015-MUS-task dataset](https://sisec.inria.fr/sisec-2015/)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [End-to-end music source separation: is it possible in the waveform domain?](http://arxiv.org/abs/1810.12187)
**Author**: Lluís, Francesc; Pons, Jordi; Serra, Xavier

**Year**: 2019
>**Abstract**: Most of the currently successful source separation techniques use the magnitude spectrogram as input, and are therefore by default omitting part of the signal: the phase. To avoid omitting potentially useful information, we study the viability of using end-to-end models for music source separation — which take into account all the information available in the raw audio signal, including the phase. Although during the last decades end-to-end music source separation has been considered almost unattainable, our results conﬁrm that waveform-based models can perform similarly (if not better) than a spectrogram-based deep learning model. Namely: a Wavenet-based model we propose and Wave-U-Net can outperform DeepConvSep, a recent spectrogram-based deep learning model.

**Data Set**: [DSD100](https://sigsep.github.io/datasets/dsd100.html)

**Source Code**: [Source Code](https://github.com/francesclluis/source-separation-wavenet)

**Demo**: [Demo](http://jordipons.me/apps/end-to-end-music-source-separation/)

#  [Model-based STFT phase recovery for audio source separation](http://arxiv.org/abs/1608.01953)
**Author**: Magron, Paul; Badeau, Roland; David, Bertrand

**Year**: 2016
>**Abstract**: This paper introduces a novel technique for reconstructing the phase of modiﬁed spectrograms of audio signals. From the analysis of mixtures of sinusoids we obtain relationships between phases of successive time frames in the Time-Frequency (TF) domain. Instantaneous frequencies are estimated locally to encompass the class of non-stationary signals such as vibratos. This technique ensures the horizontal coherence (over time) of the partials. The method is tested on a variety of data and demonstrates better performance than traditional consistencybased approaches. We also introduce an audio restoration framework and obtain results that compete with other state-of-theart methods. Finally, we apply this phase recovery method to an audio source separation task where the spectrograms of the isolated components are known. We propose to use the phase unwrapping estimate to initialize a source separation iterative procedure. Experiments conducted on realistic music pieces demonstrate the effectiveness of such a method for various music signal processing tasks.

**Data Set**: [DSD100](https://sigsep.github.io/datasets/dsd100.html), [MAPS - A piano database for multipitch estimation and automatic transcription of music,](http://www.tsi.telecom-paristech.fr/aao/en/2010/07/08/maps-database-a-piano-database-for-multipitch-estimation-and-automatic-transcription-of-music/)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Pitch-informed solo and accompaniment separation towards its use in music education applications](https://asp-eurasipjournals.springeropen.com/articles/10.1186/1687-6180-2014-23)
**Author**: Cano, Estefanía; Schuller, Gerald; Dittmar, Christian

**Year**: 2014
>**Abstract**: We present a system for the automatic separation of solo instruments and music accompaniment in polyphonic music recordings. Our approach is based on a pitch detection front-end and a tone-based spectral estimation. We assess the plausibility of using sound separation technologies to create practice material in a music education context. To better understand the sound separation quality requirements in music education, a listening test was conducted to determine the most perceptually relevant signal distortions that need to be improved. Results from the listening test show that solo and accompaniment tracks pose different quality requirements and should be optimized differently. We propose and evaluate algorithm modifications to better understand their effects on objective perceptual quality measures. Finally, we outline possible ways of optimizing our separation approach to better suit the requirements of music education applications.

**Data Set**: [TRIOS Dataset](https://c4dm.eecs.qmul.ac.uk/rdr/handle/123456789/27), [SISEC](http://sisec.wiki.irisa.fr/tiki-index.php?page=Professiolly%20produced%20music%20recordings), [CCMixter database](http://dig.ccmixter.org/)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Melody Extraction from Polyphonic Music Signals using Pitch Contour Characteristics](http://www.mtg.upf.edu/system/files/publications/SalamonGomezMelodyTASLP2012.pdf)
**Author**: Salamon, Justin; Gomez, Emilia

**Year**: 2010
>**Abstract**: We present a novel system for the automatic extraction of the main melody from polyphonic music recordings. Our approach is based on the creation and characterisation of pitch contours, time continuous sequences of pitch candidates grouped using auditory streaming cues. We deﬁne a set of contour characteristics and show that by studying their distributions we can devise rules to distinguish between melodic and non-melodic contours. This leads to the development of new voicing detection, octave error minimisation and melody selection techniques.

**Data Set**: Not availabe

**Source Code**: [Source Code](https://www.music-ir.org/mirex/wiki/MIREX_HOME)

**Demo**: [Demo](https://www.music-ir.org/mirex/wiki/MIREX_HOME)

#  [Deep clustering and conventional networks for music separation: Stronger together](http://ieeexplore.ieee.org/document/7952118/)
**Author**: Luo, Yi; Chen, Zhuo; Hershey, John R.; Le Roux, Jonathan; Mesgarani, Nima

**Year**: 2017
>**Abstract**: Deep clustering is the ﬁrst method to handle general audio separation scenarios with multiple sources of the same type and an arbitrary number of sources, performing impressively in speaker-independent speech separation tasks. However, little is known about its effectiveness in other challenging situations such as music source separation. Contrary to conventional networks that directly estimate the source signals, deep clustering generates an embedding for each time-frequency bin, and separates sources by clustering the bins in the embedding space. We show that deep clustering outperforms conventional networks on a singing voice separation task, in both matched and mismatched conditions, even though conventional networks have the advantage of end-to-end training for best signal approximation, presumably because its more ﬂexible objective engenders better regularization. Since the strengths of deep clustering and conventional network architectures appear complementary, we explore combining them in a single hybrid network trained via an approach akin to multi-task learning. Remarkably, the combination signiﬁcantly outperforms either of its components.

**Data Set**: [DSD100](https://sigsep.github.io/datasets/dsd100.html)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Sparse Pursuit and Dictionary Learning for Blind Source Separation in Polyphonic Music Recordings](http://arxiv.org/abs/1806.00273)
**Author**: Schulze, Sören; King, Emily J.

**Year**: 2019
>**Abstract**: We propose a novel method for the blind separation of single-channel audio signals produced by the mixed sounds of musical instruments. While the approach of applying non-negative matrix factorization (NMF) has been studied in many papers, it does not make use of the pitch-invariance that the sounds of many instruments exhibit. This limitation can be overcome by using tensor factorization, in which context the use of log-frequency spectrograms was initiated, but this still requires the specific tuning of the instruments to be hard-coded into the algorithm. We develop a general-purpose sparse pursuit method that matches a discrete spectrum with given shifted continuous patterns. We first use it in order to transform our audio signal into a log-frequency spectrogram that shares properties with the mel spectrogram but is applicable to a wider frequency range. Then, we use the same algorithm to identify patterns from instrument sounds in the spectrogram. The relative amplitudes of the harmonics are saved in a dictionary, which is trained via a modified version of Adam. For a realistic monaural piece with acoustic recorder and violin, we achieve qualitatively good separation with a signal-to-distortion ratio (SDR) of 13.7 dB, a signal-to-interference ratio (SIR) of 28.1 dB, and a signal-to-artifacts ratio (SAR) of 13.9 dB, averaged over the instruments.

**Data Set**: Not availabe

**Source Code**: [Source Code](https://github.com/rgcda/Musisep)

**Demo**: [Demo](https://www.math.colostate.edu/~king/software.html#Musisep)

