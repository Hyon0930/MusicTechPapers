#2016 [WaveNet: A Generative Model for Raw Audio](http://arxiv.org/abs/1609.03499)
Author: Oord, Aaron van den; Dieleman, Sander; Zen, Heiga; Simonyan, Karen; Vinyals, Oriol; Graves, Alex; Kalchbrenner, Nal; Senior, Andrew; Kavukcuoglu, Koray
>Abstract: This paper introduces WaveNet, a deep neural network for generating raw audio waveforms. The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efﬁciently trained on data with tens of thousands of samples per second of audio. When applied to text-to-speech, it yields state-ofthe-art performance, with human listeners rating it as signiﬁcantly more natural sounding than the best parametric and concatenative systems for both English and Mandarin. A single WaveNet can capture the characteristics of many different speakers with equal ﬁdelity, and can switch between them by conditioning on the speaker identity. When trained to model music, we ﬁnd that it generates novel and often highly realistic musical fragments. We also show that it can be employed as a discriminative model, returning promising results for phoneme recognition.

Data Set: [The MagTagATune dataset](http://mirg.city.ac.uk/codeapps/the-magtagatune-dataset)

Source Code: [Source Code](https://www.deepmind.com/blog/article/wavenet-generative-model-raw-audio)

Demo: [Demo](https://www.deepmind.com/blog/article/wavenet-generative-model-raw-audio)

