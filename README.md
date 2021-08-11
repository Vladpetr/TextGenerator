# TextGenerator
A simple text generator using Markov chains

**TextGenerator** can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model.

The following operations were performed:
* [x] Open the given text corpus, break the text into separate words, and obtain some properties of the corpus.
* [x] Create a Markov chain model that shows the probability of certain words appearing after a given chain of words.
* [x] Use the Markov model to generate a text starting with a user-specified word and handle exceptions.
* [x] Modify the algorithm so that sentences always start with capital letters and end with punctuation marks.
* [x] Extend the program to create a Markov model based on trigrams in order to generate more sensible sentences.

## Technologies used

- python - version 3.8


## License

    Copyright [2021] [Vladyslav Petrenko]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
