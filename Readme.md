
## Introduction :

In the repository shared down below they are two folders namely **ASR** and **SP** in which the tasks of Automatic Speech Recognition and Signal Processing have been carried out respectively. The _SP_ folder has a folder of _outpus_ where all the graphs are stored in the format of _.png_, all the inferences are written in the Readme file for both Segments of _ASR_ and _SP_.

## ASR(Automatic Speech Recognition):

The python script _main.py_ is the core logic of computing the WER(Word Error Rate) and CER(Character Error Rate) of the given _.tsv_ files.

> Logic :

- I have used pandas and given jiwer python libraries for ASR evaluation.
- As, per the given inputs and using numpy I have had colums of _"Reference"_ and _"ASR Output"_ in a data frame.
- Combined the entire data input of each column of dataframe using _.join_ of numpy.
- By the help of imported library, we could use the predefined functions of _wer_ and _cer_ to compute Word Error Rate and Character Error Rate repectively.
- Printed the outputs of both the _.tsv_ files and have compared the same.

> Instructions :

- First imported the required libraries and then curated a function to extract the _text_ for ASR and Reference to compute WER and CER and have them as the return values of the function.
- Have run the same function for both the ASR Outputs, and compared them.

> Explanation of WER and CER :

- WER :
  - Mathematically,
    WER = $\frac{S+D+I}{N}$
    _Where_:
  - S : Number of Substituted Words (wrong words)
  - D : Number of Deleted words (missing words)
  - I : Number of Inserted words (extra words)
  - N : Total number of words in the reference transcript

Ideally, an ASR sysytem shall have zero(0) WER, which means that the transcript and the refrence script are both same and are matching with each other.It measures word level accuracy.
So, lower the WER better shall be the ASR. It's a general metric used to measure the accuracy of the ASR system.

- CER :
  - Mathematically,
    CER = $\frac{S+D+I}{N}$
    _Where_:
  - S : Number of Substituted words (wrong words)
  - D : Number of Deleted (missing words)
  - I : Number of Inserted words (extra words)
  - N : Total number of characters in the reference transcript

Similar, to WER an ideal system shall have zero(0) WER which infers that transcription and reference are same. So, lower the WER better shall be the ASR.It's a metric used to measure accuracy of fine grains of letters and also spelling. Generally, used for _Non-English_ like text languages.

> Analysis of ASR Systems:

Evaluating both the _.tsv_ files we've analyzed two(2) ASR Systems.

- The ASR System evaluation metric goes like :
  - ASR -1 :- WER : 0.2739 CER : 0.1325
  - ASR -2 :- WER : 0.4746 CER : 0.2219
- From the above data we can infer that at both character level and word level ASR-System -1 has outperformed ASR-System-2.
- Because, System 1 has lower CER it would posses a better internal phenome to character mapping.
- Lower WER of System 1 will have better contextual understanding thus will help in decoding much better.
- System-2's, higher error rate would indicate more suceptability and it's resistance towards noise.

  To finally conclude, _ASR System 1_ demonstrates superior performance with a WER of 27.4 % and CER of 13.3 %,thereby achieving roughly 40 % fewer recognition errors than _ASR System 2_.
  Which indicates that _System 1_ is significantly more reliable for transcription tasks, both at the word and character levels.

## Signal Processing Tasks :

Have used _librosa_ python library for processing and reading of the given audio signal.
Then, computed STFT on the same using the _window length_ to be 1024 and overlapping samples to be 256- also refrerred to as _hop length_.
Next, plotted and observed the RMS Energy on a decibel scale, along diffrent frames.
Atlast, plotted the given input speech and have marked the vertical lines corresponding to the _.tsv_ file.

> Spectrogram :

- This, is a demonstration of how the frequency content(Y- Axis) is varying with time(X-Axis) and amplitude on colour scale on dB(decibel) scale.
- From the spectrogram we can observe multiple bright vertical bands whose frequency content lies between 100Hz to 4kHz which predominantly indicates an human speech. And the dark bands indicate the silent regions of the speech input.
- The Bright yellow/green segments on the graph represent the voiced sounds thereby higher energy segments.
- The dark blue/purple segments represent the lower energy segements which mean they include un-voiced, silent regions which also caputures silence and pause breaks taken by the subject.

> RMS Energy :

- The _-10 dB_ speech region is the place where the speaker is predominantly speaking with active voice, and the intervals where the energy falls to _-70 dB_ to _-80dB_ is the place are the silent regions which inturn represent pauses, gaps, or background silence.
- There are multiple _discrete low energy valleys_ which could be inferred to as Natural speech pauses, low background noise.
- There are no sudden drops in energy which could imply that _stable recording_ was performed with subject. Repetition of high–low patterns shows structured speech fit for speech analysis.
- The dynamic energy range of (0 to -80 dB) spans to a segment of _0 to -10 dB_ as active region - voiced speech, _-20dB to 40dB_ as for unvoiced speech, and _<40 dB_ associated with silence or no speech.

> Waveform of Speech :

- We can observe that they are _9(nine)_ active regions of the speech which clearly correlated with given _.tsv_ file.
- The silent and active regions exactly allign with the _ASR_ output.
- There by the temporal characteristics could be clearly observed from the graph.
- No markable _dc offset_ is observed and the waveform is centered around zero(0).

The above are the inferences which are made to the given audio input waveform by generating _Spectrogram_, _RMS Energy_ and _waveform_ correlated with the ASR output.
