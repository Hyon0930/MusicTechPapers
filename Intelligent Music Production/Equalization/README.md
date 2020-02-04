#  [All About Audio Equalization: Solutions and Frontiers](http://www.mdpi.com/2076-3417/6/5/129)
**Author**: Välimäki, Vesa; Reiss, Joshua

**Year**: 2016
>**Abstract**: Audio equalization is a vast and active research area. The extent of research means that one often cannot identify the preferred technique for a particular problem. This review paper bridges those gaps, systemically providing a deep understanding of the problems and approaches in audio equalization, their relative merits and applications. Digital signal processing techniques for modifying the spectral balance in audio signals and applications of these techniques are reviewed, ranging from classic equalizers to emerging designs based on new advances in signal processing and machine learning. Emphasis is placed on putting the range of approaches within a common mathematical and conceptual framework. The application areas discussed herein are diverse, and include well-deﬁned, solvable problems of ﬁlter design subject to constraints, as well as newly emerging challenges that touch on problems in semantics, perception and human computer interaction. Case studies are given in order to illustrate key concepts and how they are applied in practice. We also recommend preferred signal processing approaches for important audio equalization problems. Finally, we discuss current challenges and the uncharted frontiers in this ﬁeld. The source code for methods discussed in this paper is made available at https://code.soundsoftware.ac.uk/projects/allaboutaudioeq.

**Data Set**: [SocialEQ](http://www.markcartwright.com/research/socialeq)

**Source Code**: [Source Code](https://code.soundsoftware.ac.uk/projects/allaboutaudioeq)

**Demo**: Not availabe

#  [Automatic equalization of multi-channel audio using cross-adaptive methods](http://www.aes.org/e-lib/browse.cfm?elib=15026)
**Author**: Perez, Enrique; Reiss, Joshua

**Year**: 2009
>**Abstract**: A method for automatically equalizing a multi-track mixture has been implemented. The method aims to achieve equal average perceptual loudness on all frequencies amongst all multi-track channels. The method uses accumulative spectral decomposition techniques together with cross-adaptive audio effects to achieve equalization. The method has applications in live and recorded audio mixing where the audio engineer would like to reduce set-up time, or as a tool for inexperienced users wishing to perform audio mixing. Results are reported which show how the frequency content of each channel is modified, and which demonstrate the ability of the automatic equalization method to achieve a well-balanced and equalized final mix.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Implementation of an intelligent equalization tool using Yule-Walker for music mixing and mastering](http://www.aes.org/e-lib/browse.cfm?elib=16792)
**Author**: Ma, Zheng; Reiss, Joshua D; Black, Dawn A A

**Year**: 2013
>**Abstract**: A new approach for automatically equalizing an audio signal towards a target frequency spectrum is presented. The algorithm is based on the Yule-Walker method and designs recursive IIR digital filters using Least-Squares fitting to any desired frequency response. The target equalization curve is obtained from the spectral distribution analysis of a large dataset of popular commercial recordings. A real-time C++ VST plug-in and an off-line Matlab implementation have been created. Straightforward objective evaluation is provided, where the output frequency spectra are compared against the target equalization curve and the ones produced by an alternative equalization method.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Design of Audio Parametric Equalizer Filters Directly in the Digital Domain](http://ieeexplore.ieee.org/document/5629354/)
**Author**: Reiss, Joshua D.

**Year**: 2011
>**Abstract**: Most design procedures for a digital parametric equalizer begin with analog design techniques, followed by applying the bilinear transform to an analog prototype. As an alternative, an approximation to the parametric equalizer is sometimes designed using pole-zero placement techniques. In this paper, we present an exact derivation of the parametric equalizer without resorting to an analog prototype. We show that there are many solutions to the parametric equalizer design constraints as usually stated, but only one of which consistently yields stable, minimum phase bbehaviorwith the upper and lower cutoff frequencies positioned around the center frequency. The conditions for complex conjugate poles and zeros are found and the resultant pole zero placements are examined.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Autonomous Multitrack Equalization Based on Masking Reduction](http://www.aes.org/e-lib/browse.cfm?elib=17637)
**Author**: Hafezi, Sina; Reiss, Joshua

**Year**: 2015
>**Abstract**: Spectral masking is when the threshold of audibility for one sound is raised by the simultaneous presence of another sound. In multitrack music production, this results in less ability to fully hear and distinguish the sound sources in the mix. We design a simplified measure of masking based on best practices in sound engineering. We implement both off-line and realtime, low latency autonomous multitrack equalization systems to reduce masking in multitrack audio. We perform objective measurement of the spectral masking in the resultant mixes and conduct a listening test for subjective comparison between the mix results of different implementations of our system, a raw mix, and manual mixes made by an amateur and a professional mix engineer. The results show that autonomous systems reduce both the perceived masking and objective spectral masking and improve the overall quality of the mix. We show that our offline semi-autonomous system is capable of improving the raw mix better than an amateur and close to a professional mix by simply controlling one user parameter. Our results also suggest that existing objective measures of masking are ill-suited for quantifying perceived masking in multitrack musical audio.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Automatic Target Mixing using Least-Squares Optimization of Gains and Equalization Settings](https://www.eecs.qmul.ac.uk/~josh/documents/2009/BarchiesiReiss-AutomaticTargetMixing.pdf)
**Author**: Barchiesi, Daniele; Reiss, Josh

**Year**: 2009
>**Abstract**: The proposed automatic target mixing algorithm determines the gains and the equalization settings for the mixing of a multi-track recording using a least-squares optimization. These parameters are estimated using a single channel target mix, that is a signal which contains the same audio tracks as the multi-track recording, but that has been previously mixed using some unknown settings.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Modeling the Harmonic Exciter](http://www.aes.org/e-lib/browse.cfm?elib=16939)
**Author**: Shekar, Priyanka; Smith, Julius

**Year**: 2013
>**Abstract**: A harmonic exciter is an audio eﬀects signal processor applied to enhance the brightness and clarity of a sound, particularly used for vocals. This is achieved by inducing a measured amount of high-frequency distortion. In this paper, an exciter is digitally modeled and implemented as a standalone application (or plugin) using the FAUST (Functional AUdio STream) programming language for real-time audio. The model is based on the Aural Exciter by Aphex Ltd., an analog hardware unit. Technical speciﬁcations of the Aural Exciter are drawn from the original 1979 patent. The digital model performs as expected, recreating a “vintage” style audio eﬀect.

**Data Set**: Not availabe

**Source Code**: [Source Code](https://github.com/grame-cncm/faust)

**Demo**: Not availabe

#  [END-TO-END EQUALIZATION WITH CONVOLUTIONAL NEURAL NETWORKS](http://dafx2018.web.ua.pt/papers/DAFx2018_paper_27.pdf)
**Author**: Campos, Guilherme; Fonseca, Nuno; Ferreira, Anibal; Davies, Matthew

**Year**: 2018
>**Abstract**: This work aims to implement a novel deep learning architecture to perform audio processing in the context of matched equalization. Most existing methods for automatic and matched equalization show effective performance and their goal is to ﬁnd a respective transfer function given a frequency response. Nevertheless, these procedures require a prior knowledge of the type of ﬁlters to be modeled. In addition, ﬁxed ﬁlter bank architectures are required in automatic mixing contexts. Based on end-to-end convolutional neural networks, we introduce a general purpose architecture for equalization matching. Thus, by using an end-toend learning approach, the model approximates the equalization target as a content-based transformation without directly ﬁnding the transfer function. The network learns how to process the audio directly in order to match the equalized target audio. We train the network through unsupervised and supervised learning procedures. We analyze what the model is actually learning and how the given task is accomplished. We show the model performing matched equalization for shelving, peaking, lowpass and highpass IIR and FIR equalizers.

**Data Set**: [Salamander Grand Piano V3 dataset](https://musical-artifacts.com/artifacts/3)

**Source Code**: Not availabe

**Demo**: Not availabe

