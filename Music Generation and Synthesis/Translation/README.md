#  [Music Transformer](http://arxiv.org/abs/1809.04281)
**Author**: Huang, Cheng-Zhi Anna; Vaswani, Ashish; Uszkoreit, Jakob; Shazeer, Noam; Simon, Ian; Hawthorne, Curtis; Dai, Andrew M.; Hoffman, Matthew D.; Dinculescu, Monica; Eck, Douglas

**Year**: 2018
>**Abstract**: Music relies heavily on repetition to build structure and meaning. Self-reference occurs on multiple timescales, from motifs to phrases to reusing of entire sections of music, such as in pieces with ABA structure. The Transformer (Vaswani et al., 2017), a sequence model based on self-attention, has achieved compelling results in many generation tasks that require maintaining long-range coherence. This suggests that self-attention might also be well-suited to modeling music. In musical composition and performance, however, relative timing is critically important. Existing approaches for representing relative positional information in the Transformer modulate attention based on pairwise distance (Shaw et al., 2018). This is impractical for long sequences such as musical compositions since their memory complexity for intermediate relative information is quadratic in the sequence length. We propose an algorithm that reduces their intermediate memory requirement to linear in the sequence length. This enables us to demonstrate that a Transformer with our modiﬁed relative attention mechanism can generate minutelong compositions (thousands of steps, four times the length modeled in Oore et al. (2018)) with compelling structure, generate continuations that coherently elaborate on a given motif, and in a seq2seq setup generate accompaniments conditioned on melodies1. We evaluate the Transformer with our relative attention mechanism on two datasets, JSB Chorales and Piano-e-Competition, and obtain state-of-the-art results on the latter.

**Data Set**: [J.S. Bach chorales dataset](https://github.com/czhuang/JSB-Chorales-dataset), [Piano-e-Competition dataset](http://www.piano-e-competition.com/)

**Source Code**: Not availabe

**Demo**: [Demo](https://storage.googleapis.com/music-transformer/index.html)

#  [A Universal Music Translation Network](http://arxiv.org/abs/1805.07848)
**Author**: Mor, Noam; Wolf, Lior; Polyak, Adam; Taigman, Yaniv

**Year**: 2018
>**Abstract**: We present a method for translating music across musical instruments, genres, and styles. This method is based on a multi-domain wavenet autoencoder, with a shared encoder and a disentangled latent space that is trained end-to-end on waveforms. Employing a diverse training dataset and large net capacity, the domain-independent encoder allows us to translate even from musical domains that were not seen during training. The method is unsupervised and does not rely on supervision in the form of matched samples between domains or musical transcriptions. We evaluate our method on NSynth, as well as on a dataset collected from professional musicians, and achieve convincing translations, even when translating from whistling, potentially enabling the creation of instrumental music by untrained humans.

**Data Set**: [The NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth)

**Source Code**: Not availabe

**Demo**: [Demo](https://www.youtube.com/watch?v=vdxCqNWTpUs&feature=youtu.be)

