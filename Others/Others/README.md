#  [Autoencoders for music sound modeling: a comparison of linear, shallow, deep, recurrent and variational models](https://arxiv.org/abs/1806.04096)
**Author**: Roche, Fanny; Hueber, Thomas; Limier, Samuel; Girin, Laurent

**Year**: 2019
>**Abstract**: This study investigates the use of non-linear unsupervised dimensionality reduction techniques to compress a music dataset into a low-dimensional representation which can be used in turn for the synthesis of new sounds. We systematically compare (shallow) autoencoders (AEs), deep autoencoders (DAEs), recurrent autoencoders (with Long ShortTerm Memory cells – LSTM-AEs) and variational autoencoders (VAEs) with principal component analysis (PCA) for representing the high-resolution short-term magnitude spectrum of a large and dense dataset of music notes into a lower-dimensional vector (and then convert it back to a magnitude spectrum used for sound resynthesis). Our experiments were conducted on the publicly available multiinstrument and multi-pitch database NSynth. Interestingly and contrary to the recent literature on image processing, we can show that PCA systematically outperforms shallow AE. Only deep and recurrent architectures (DAEs and LSTM-AEs) lead to a lower reconstruction error. The optimization criterion in VAEs being the sum of the reconstruction error and a regularization term, it naturally leads to a lower reconstruction accuracy than DAEs but we show that VAEs are still able to outperform PCA while providing a low-dimensional latent space with nice “usability” properties. We also provide corresponding objective measures of perceptual audio quality (PEMO-Q scores), which generally correlate well with the reconstruction error.

**Data Set**: [NSynth dataset](https://magenta.tensorflow.org/datasets/nsynth)

**Source Code**: Not availabe

**Demo**: [Demo 1](http://www.gipsa-lab.fr/~fanny.roche/SMC_2019.html)

#  [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576)
**Author**: Gatys, Leon A.; Ecker, Alexander S.; Bethge, Matthias

**Year**: 2015
>**Abstract**: In fine art, especially painting, humans have mastered the skill to create unique visual experiences through composing a complex interplay between the content and style of an image. Thus far the algorithmic basis of this process is unknown and there exists no artificial system with similar capabilities. However, in other key areas of visual perception such as object and face recognition near-human performance was recently demonstrated by a class of biologically inspired vision models called Deep Neural Networks. Here we introduce an artificial system based on a Deep Neural Network that creates artistic images of high perceptual quality. The system uses neural representations to separate and recombine content and style of arbitrary images, providing a neural algorithm for the creation of artistic images. Moreover, in light of the striking similarities between performance-optimised artificial neural networks and biological vision, our work offers a path forward to an algorithmic understanding of how humans create and perceive artistic imagery.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: Not availabe

