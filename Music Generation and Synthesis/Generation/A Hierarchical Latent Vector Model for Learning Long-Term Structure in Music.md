#2018 [A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music](http://arxiv.org/abs/1803.05428)
Author: Roberts, Adam; Engel, Jesse; Raffel, Colin; Hawthorne, Curtis; Eck, Douglas
>Abstract: The Variational Autoencoder (VAE) has proven to be an effective model for producing semantically meaningful latent representations for natural data. However, it has thus far seen limited application to sequential data, and, as we demonstrate, existing recurrent VAE models have difficulty modeling sequences with long-term structure. To address this issue, we propose the use of a hierarchical decoder, which first outputs embeddings for subsequences of the input and then uses these embeddings to generate each subsequence independently. This structure encourages the model to utilize its latent code, thereby avoiding the "posterior collapse" problem which remains an issue for recurrent VAEs. We apply this architecture to modeling sequences of musical notes and find that it exhibits dramatically better sampling, interpolation, and reconstruction performance than a "flat" baseline model. An implementation of our "MusicVAE" is available online at http://g.co/magenta/musicvae-code.

Data Set: [Lakh MIDI Dataset](https://colinraffel.com/projects/lmd/)

Source Code: [Source Code](https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae)

Demo: [Demo](https://storage.googleapis.com/magentadata/papers/musicvae/index.html)

