#  [Audio Declipping by Cosparse Hard Thresholding](https://pdfs.semanticscholar.org/938f/24eb12c66bf4d8f81ddcbbecb9ce268e6b45.pdf?_ga=2.194532077.1935390015.1574141093-1556478679.1573971532)
Author: Kitić, Srđan; Bertin, Nancy; Gribonval, Rémi

Year: 2014
>Abstract: Recovery of clipped audio signals is a very challenging inverse problem. Recently, it has been successfully addressed by several methods based on the sparse synthesis data model. In this work we propose an algorithm for enhancement of clipped audio signals that exploits the sparse analysis (cosparse) data model. Experiments on real audio data indicate that the algorithm has better signal restoration performance than state-of-the-art sparse synthesis declipping methods.

Data Set: Not availabe

Source Code: Not availabe

Demo: [Demo](https://spade.inria.fr/)

#  [Efficient audio declipping using regularized least squares](http://ieeexplore.ieee.org/document/7177964/)
Author: Harvilla, Mark J.; Stern, Richard M.

Year: 2015
>Abstract: While many recently proposed audio declipping algorithms are highly effective in their ability to restore clipped speech, the algorithms’ computational complexities inhibit their use in many practical situations. Real-time or nearly real-time performance is impossible using a typical laptop computer, with some algorithms taking as long as 400 times the actual duration of the input to complete restoration. This paper introduces a novel declipping algorithm, referred to as Regularized Blind Amplitude Reconstruction, which is capable of restoring clipped audio at rates much faster than real time and at restoration qualities comparable to existing algorithms. The quality of declipping is evaluated in terms of automatic speech recognition performance on declipped speech, as well as the degree to which each declipping algorithm improves the audio’s signal-to-noise ratio.

Data Set: [Resource Magement Database](http://www.speech.cs.cmu.edu/databases/rm1/)

Source Code: Not availabe

Demo: Not availabe

#  [An Efficient Algorithm for Clipping Detection and Declipping Audio](http://www.aes.org/e-lib/browse.cfm?elib=18486)
Author: Dukes, Bob

Year: 2016
>Abstract: We present an algorithm for end to end declipping, which includes clipping detection and the replacement of clipped samples. To detect regions of clipping, we analyze the signal’s amplitude histogram and the shape of the signal in the time-domain. The sample replacement algorithm uses a two-pass approach: short regions of clipping are replaced in the time-domain and long regions of clipping are replaced in the frequency-domain. The algorithm is robust against different types of clipping and is efficient compared to existing approaches. The algorithm has been implemented in an open source JavaScript client-side web application. Clipping detection is shown to give an f-measure of 0.92 and is robust to the clipping level.

Data Set: [Music Audio Benchmark Data Set](https://www-ai.cs.tu-dortmund.de/audio.html)

Source Code: Not availabe

Demo: Not availabe

#  [Revisiting Synthesis Model of Sparse Audio Declipper](http://arxiv.org/abs/1807.03612)
Author: Záviška, Pavel; Rajmic, Pavel; Průša, Zdeněk; Veselý, Vítězslav

Year: 2018
>Abstract: The state of the art in audio declipping has currently been achieved by SPADE (SParse Audio DEclipper) algorithm by Kiti´c et al. Until now, the synthesis/sparse variant, S-SPADE, has been considered signiﬁcantly slower than its analysis/cosparse counterpart, A-SPADE. It turns out that the opposite is true: by exploiting a recent projection lemma, individual iterations of both algorithms can be made equally computationally expensive, while S-SPADE tends to require considerably fewer iterations to converge. In this paper, the two algorithms are compared across a range of parameters such as the window length, window overlap and redundancy of the transform. The experiments show that although S-SPADE typically converges faster, the average performance in terms of restoration quality is not superior to A-SPADE.

Data Set: Not availabe

Source Code: [http://www.utko.feec.vutbr.cz/~rajmic/software/aspade_vs_sspade.zip]()

Demo: Not availabe

#  [Consistent Iterative Hard Thresholding For Signal Declipping](http://arxiv.org/abs/1303.1023)
Author: Kitić, Srdjan; Jacques, Laurent; Madhu, Nilesh; Hopwood, Michael Peter; Spriet, Ann; De Vleeschouwer, Christophe

Year: 2013
>Abstract: Clipping or saturation in audio signals is a very common problem in signal processing, for which, in the severe case, there is still no satisfactory solution. In such case, there is a tremendous loss of information, and traditional methods fail to appropriately recover the signal. We propose a novel approach for this signal restoration problem based on the framework of Iterative Hard Thresholding. This approach, which enforces the consistency of the reconstructed signal with the clipped observations, shows superior performance in comparison to the state-of-the-art declipping algorithms. This is conﬁrmed on synthetic and on actual high-dimensional audio data processing, both on SNR and on subjective user listening evaluations.

Data Set: Not availabe

Source Code: Not availabe

Demo: Not availabe

#  [Audio Declipping by Cosparse Hard Thresholding](https://pdfs.semanticscholar.org/938f/24eb12c66bf4d8f81ddcbbecb9ce268e6b45.pdf?_ga=2.194532077.1935390015.1574141093-1556478679.1573971532)
Author: Kitić, Srđan; Bertin, Nancy; Gribonval, Rémi

Year: 2014
>Abstract: Recovery of clipped audio signals is a very challenging inverse problem. Recently, it has been successfully addressed by several methods based on the sparse synthesis data model. In this work we propose an algorithm for enhancement of clipped audio signals that exploits the sparse analysis (cosparse) data model. Experiments on real audio data indicate that the algorithm has better signal restoration performance than state-of-the-art sparse synthesis declipping methods.

Data Set: Not availabe

Source Code: Not availabe

Demo: [Demo](https://spade.inria.fr/)

#  [Efficient audio declipping using regularized least squares](http://ieeexplore.ieee.org/document/7177964/)
Author: Harvilla, Mark J.; Stern, Richard M.

Year: 2015
>Abstract: While many recently proposed audio declipping algorithms are highly effective in their ability to restore clipped speech, the algorithms’ computational complexities inhibit their use in many practical situations. Real-time or nearly real-time performance is impossible using a typical laptop computer, with some algorithms taking as long as 400 times the actual duration of the input to complete restoration. This paper introduces a novel declipping algorithm, referred to as Regularized Blind Amplitude Reconstruction, which is capable of restoring clipped audio at rates much faster than real time and at restoration qualities comparable to existing algorithms. The quality of declipping is evaluated in terms of automatic speech recognition performance on declipped speech, as well as the degree to which each declipping algorithm improves the audio’s signal-to-noise ratio.

Data Set: [Resource Magement Database](http://www.speech.cs.cmu.edu/databases/rm1/)

Source Code: Not availabe

Demo: Not availabe

#  [An Efficient Algorithm for Clipping Detection and Declipping Audio](http://www.aes.org/e-lib/browse.cfm?elib=18486)
Author: Dukes, Bob

Year: 2016
>Abstract: We present an algorithm for end to end declipping, which includes clipping detection and the replacement of clipped samples. To detect regions of clipping, we analyze the signal’s amplitude histogram and the shape of the signal in the time-domain. The sample replacement algorithm uses a two-pass approach: short regions of clipping are replaced in the time-domain and long regions of clipping are replaced in the frequency-domain. The algorithm is robust against different types of clipping and is efficient compared to existing approaches. The algorithm has been implemented in an open source JavaScript client-side web application. Clipping detection is shown to give an f-measure of 0.92 and is robust to the clipping level.

Data Set: [Music Audio Benchmark Data Set](https://www-ai.cs.tu-dortmund.de/audio.html)

Source Code: Not availabe

Demo: Not availabe

#  [Revisiting Synthesis Model of Sparse Audio Declipper](http://arxiv.org/abs/1807.03612)
Author: Záviška, Pavel; Rajmic, Pavel; Průša, Zdeněk; Veselý, Vítězslav

Year: 2018
>Abstract: The state of the art in audio declipping has currently been achieved by SPADE (SParse Audio DEclipper) algorithm by Kiti´c et al. Until now, the synthesis/sparse variant, S-SPADE, has been considered signiﬁcantly slower than its analysis/cosparse counterpart, A-SPADE. It turns out that the opposite is true: by exploiting a recent projection lemma, individual iterations of both algorithms can be made equally computationally expensive, while S-SPADE tends to require considerably fewer iterations to converge. In this paper, the two algorithms are compared across a range of parameters such as the window length, window overlap and redundancy of the transform. The experiments show that although S-SPADE typically converges faster, the average performance in terms of restoration quality is not superior to A-SPADE.

Data Set: Not availab#  [Sparsity and Cosparsity for Audio Declipping: A Flexible Non-convex Approach](https://arxiv.org/abs/1506.01830)
Author: Kitić, Srđan; Bertin, Nancy; Gribonval, Rémi

Year: 2015
>Abstract: This work investigates the empirical performance of the sparse synthesis versus sparse analysis regularization for the ill-posed inverse problem of audio declipping. We develop a versatile non-convex heuristics which can be readily used with both data models. Based on this algorithm, we report that, in most cases, the two models perform almost similarly in terms of signal enhancement. However, the analysis version is shown to be amenable for real time audio processing, when certain analysis operators are considered. Both versions outperform state-of-the-art methods in the ﬁeld, especially for the severely saturated signals.

Data Set: [RWC music database](https://staff.aist.go.jp/m.goto/RWC-MDB/)

Source Code: Not availabe

Demo: Not availabe

#  [Consistent Dictionary Learning for Signal Declipping](http://epubs.surrey.ac.uk/846156/1/Consistent_DL_for_signal_declipping.pdf)
Author: Rencker, Lucas; Bach, Francis; Wang, Wenwu; Plumbley, Mark D.

Year: 2018
>Abstract: Clipping, or saturation, is a common nonlinear distortion in signal processing. Recently, declipping techniques have been proposed based on sparse decomposition of the clipped signals on a ﬁxed dictionary, with additional constraints on the amplitude of the clipped samples. Here we propose a dictionary learning approach, where the dictionary is directly learned from the clipped measurements. We propose a softconsistency metric that minimizes the distance to a convex feasibility set, and takes into account our knowledge about the clipping process. We then propose a gradient descent-based dictionary learning algorithm that minimizes the proposed metric, and is thus consistent with the clipping measurement. Experiments show that the proposed algorithm outperforms other dictionary learning algorithms applied to clipped signals. We also show that learning the dictionary directly from the clipped signals outperforms consistent sparse coding with a ﬁxed dictionary.

Data Set: Not availabe

Source Code: [Source Code](https://www.cvssp.org/Persol/LucasRencker/software.html)

Demo: [Demo](https://www.cvssp.org/Persol/LucasRencker/software.html)

