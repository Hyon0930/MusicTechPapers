#  [WaveNet: A Generative Model for Raw Audio](http://arxiv.org/abs/1609.03499)
**Author**: Oord, Aaron van den; Dieleman, Sander; Zen, Heiga; Simonyan, Karen; Vinyals, Oriol; Graves, Alex; Kalchbrenner, Nal; Senior, Andrew; Kavukcuoglu, Koray

**Year**: 2016
>**Abstract**: This paper introduces WaveNet, a deep neural network for generating raw audio waveforms. The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efﬁciently trained on data with tens of thousands of samples per second of audio. When applied to text-to-speech, it yields state-ofthe-art performance, with human listeners rating it as signiﬁcantly more natural sounding than the best parametric and concatenative systems for both English and Mandarin. A single WaveNet can capture the characteristics of many different speakers with equal ﬁdelity, and can switch between them by conditioning on the speaker identity. When trained to model music, we ﬁnd that it generates novel and often highly realistic musical fragments. We also show that it can be employed as a discriminative model, returning promising results for phoneme recognition.

**Data Set**: [The MagTagATune dataset](http://mirg.city.ac.uk/codeapps/the-magtagatune-dataset)

**Source Code**: [Source Code](https://www.deepmind.com/blog/article/wavenet-generative-model-raw-audio)

**Demo**: [Demo](https://www.deepmind.com/blog/article/wavenet-generative-model-raw-audio)

#  [Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders](http://arxiv.org/abs/1704.01279)
**Author**: Engel, Jesse; Resnick, Cinjon; Roberts, Adam; Dieleman, Sander; Eck, Douglas; Simonyan, Karen; Norouzi, Mohammad

**Year**: 2017
>**Abstract**: Generative models in vision have seen rapid progress due to algorithmic improvements and the availability of high-quality image datasets. In this paper, we oﬀer contributions in both these areas to enable similar progress in audio modeling. First, we detail a powerful new WaveNet-style autoencoder model that conditions an autoregressive decoder on temporal codes learned from the raw audio waveform. Second, we introduce NSynth, a large-scale and high-quality dataset of musical notes that is an order of magnitude larger than comparable public datasets. Using NSynth, we demonstrate improved qualitative and quantitative performance of the WaveNet autoencoder over a well-tuned spectral autoencoder baseline. Finally, we show that the model learns a manifold of embeddings that allows for morphing between instruments, meaningfully interpolating in timbre to create new types of sounds that are realistic and expressive.

**Data Set**: [The NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth)

**Source Code**: Not availabe

**Demo**: Not availabe

#  [Style Imitation and Chord Invention in Polyphonic Music with Exponential Families](http://arxiv.org/abs/1609.05152)
**Author**: Hadjeres, Gaëtan; Sakellariou, Jason; Pachet, François

**Year**: 2016
>**Abstract**: Modeling polyphonic music is a particularly challenging task because of the intricate interplay between melody and harmony. A good model should satisfy three requirements: statistical accuracy (capturing faithfully the statistics of correlations at various ranges, horizontally and vertically), ﬂexibility (coping with arbitrary user constraints), and generalization capacity (inventing new material, while staying in the style of the training corpus). Models proposed so far fail on at least one of these requirements. We propose a statistical model of polyphonic music, based on the maximum entropy principle. This model is able to learn and reproduce pairwise statistics between neighboring note events in a given corpus. The model is also able to invent new chords and to harmonize unknown melodies. We evaluate the invention capacity of the model by assessing the amount of cited, re-discovered, and invented chords on a corpus of Bach chorales. We discuss how the model enables the user to specify and enforce user-deﬁned constraints, which makes it useful for style-based, interactive music generation.

**Data Set**: Not availabe

**Source Code**: Not availabe

**Demo**: [Demo](https://flowmachines.jimdo.com/)

#  [The challenge of realistic music generation: modelling raw audio at scale](https://arxiv.org/abs/1806.10474)
**Author**: Dieleman, Sander

**Year**: 2018
>**Abstract**: Realistic music generation is a challenging task. When building generative models of music that are learnt from data, typically high-level representations such as scores or MIDI are used that abstract away the idiosyncrasies of a particular performance. But these nuances are very important for our perception of musicality and realism, so in this work we embark on modelling music in the raw audio domain. It has been shown that autoregressive models excel at generating raw audio waveforms of speech, but when applied to music, we ﬁnd them biased towards capturing local signal structure at the expense of modelling long-range correlations. This is problematic because music exhibits structure at many different timescales. In this work, we explore autoregressive discrete autoencoders (ADAs) as a means to enable autoregressive models to capture long-range correlations in waveforms. We ﬁnd that they allow us to unconditionally generate piano music directly in the raw audio domain, which shows stylistic consistency across tens of seconds.

**Data Set**: [solo piano music](https://bit.ly/2IPXoDu)

**Source Code**: Not availabe

**Demo**: [Demo](https://drive.google.com/drive/folders/1NY3MTkOSodz_5eCkjtoHUGYSulR25QGU)

#  [A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music](http://arxiv.org/abs/1803.05428)
**Author**: Roberts, Adam; Engel, Jesse; Raffel, Colin; Hawthorne, Curtis; Eck, Douglas

**Year**: 2018
>**Abstract**: The Variational Autoencoder (VAE) has proven to be an effective model for producing semantically meaningful latent representations for natural data. However, it has thus far seen limited application to sequential data, and, as we demonstrate, existing recurrent VAE models have difficulty modeling sequences with long-term structure. To address this issue, we propose the use of a hierarchical decoder, which first outputs embeddings for subsequences of the input and then uses these embeddings to generate each subsequence independently. This structure encourages the model to utilize its latent code, thereby avoiding the "posterior collapse" problem which remains an issue for recurrent VAEs. We apply this architecture to modeling sequences of musical notes and find that it exhibits dramatically better sampling, interpolation, and reconstruction performance than a "flat" baseline model. An implementation of our "MusicVAE" is available online at http://g.co/magenta/musicvae-code.

**Data Set**: [Lakh MIDI Dataset](https://colinraffel.com/projects/lmd/)

**Source Code**: [Source Code](https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae)

**Demo**: [Demo](https://storage.googleapis.com/magentadata/papers/musicvae/index.html)

