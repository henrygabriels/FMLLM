# FMLLM

**FML LM**: or, FML, this kind of looks like a Fibonacci Language Model. Can anyone help me work out if it is meaningful? 

## The Experiment

Over the last week or so, as an experiment, I took 4mb of text data from a selection of prose that I thought was interesting. I'm not sure if the results are or not.

I got Claude to write a script that looked for the words within that 4mb of text data which appeared, most often, at Fibonacci intervals to each individual word, both forwards and backwards in the text.

The output of the script was a 100mb pkg model.

## The Origin Story

The idea came from an exercise I used to do all the time. I'm a novelist (hence not knowing lots of the right words for maths / data stuff), and when I was learning to write novels, I used to make big spreadsheets of where each important word (for example "green" in Gatsby) happened, and how it recurred, and how that happened in relation to other important words in the text.

When you plotted that out, it used to often make rough - but clear - spiral shapes. I was thinking about that exercise, and whether I could use a computer to see if there were meaningful positional relationships between words that occurred at certain intervals.

One of the rules of the exercise was: no words that occur directly before or after the input word, unless they appear at a Fib interval to one of the other input words.

Finally, I added some manual weighting to particular intervals that I have often seen as being important.

## Word Generation Example

Here's an example. "Television" gives:

**Input:** `"television"`

**Output:** `"television producer widest impunity exposure autobiographical suffering scrutinizing vulgarity worship america cannot gratify electromagnetic impulses menu pass chain reprinted syndicate pursues endocrinology clinics reinforced channels trend assail possesses icons costume ordeal internet cleave revisit ambition temples crafted intermittent seek dustheaps embody compounded moral defects learns debauch vacuum gland angels primitively beautyrest mattress thank chess distaff depersonalization couture excerpt transience remain suited chromatography resolves dismantling wrestle riddle blower holocaust"`

Which is cool. And felt weirdly coherent, thematically.

*NB - I tried to filter both names and stop-words from this output.*

## Building Sentences

I wondered if I could make it write a sentence. So I got some stop-words from the library NLTK and then used the library Spacey to tell me whether a word was a verb, adjective, whatever.

I wrote some super basic grammar rules for sentences, then wrote a script that generated a variety of possible sentences from the available words. After that, I used a 100mb sentencetransformers library to rank the generated sentences for "this seems like a real sentence". I pretty aggressively capped the number of possible sentences it could consider, though the grammar rules meant that not many could be generated anyway.

I also added a new process, where each generated word - if you ask for more than one - creates a new set of possible words to select from for the next. This felt more like what sentences do. So it used a rolling but capped number of linked words, plus the NLTK stop-words, to ensure that it wasn't just choosing perfect words using the sentencetransformers filter from all 700k possible words.

### Sentence Example

**Input:** `"sarah loves my french toast"`

**Output:** `"sarah loves my french toast a piney connubial produit"`

*(I was making breakfast for my fiancee at the time.)*

This is cool, because in the training data, there isn't anything about french toast. So it's satisfying, I think, that it used 'piney' for maple syrup, and 'connubial' for loves, and 'produit', which is the French word for product. But I don't know - people see what they want to see. And the sentencetransformers model is obviously looking for semantic coherence from the candidates!

## Adding Punctuation

But, because of the weird coherence, I wanted to see if I could add punctuation to the output. Because if it could have punctuation, then it could start a new sentence by itself, maybe.

So using the same 4mb of text data, and learning only common Fib intervals (beginning at 2) for punctuation placement, I 'trained' a new 'model', which came out at 30mb.

This is where it got a bit weirder, I think, because the results seem uncannily accurate.

Again, I do think sometimes the human mind sees what it wants to see, especially with language.

But, also, I don't know, man.

### Punctuation Examples

| Input | Output |
|-------|--------|
| `We waited all night but no one ever came` | `we waited all night, but no one ever came` |
| `He smiled at me his eyes colder than winter ice` | `he smiled. at me. his eyes colder than winter, ice` |
| `I was certain the key was here but it vanished` | `i was certain the key was here. but it vanished` |
| `If you find the map do not tell anyone else` | `if you find the map do not tell anyone else.` |
| `The streets were quiet until a scream broke the silence` | `the streets, were quiet until a scream. broke the silence.` |

Really weird, I think, even though it's clearly imperfect. But I didn't expect it to be anywhere close to correct, ever.

## Limitations and Next Steps

On a novelist salary, I don't personally have the resources to test its efficacy properly. I wouldn't trust myself to do that, either, because I'm not a data scientist.

The BERT model for punctuation reconstruction is 1gb, though, so maybe it would be a kind of interesting thing for someone to try, if they'd like to reach out.

## Final Thoughts

I'm not saying there is a hidden golden ratio logic to (the English) language. And I'm definitely not claiming this is a new kind of Fibonacci machine learning language model (FML LM?).

But, from what I understand about LLMs, more input data will always mean more bloat, more training time, etc, because you're looking at words that are right next to each other. Instinctively, language doesn't work like that, the same way music and painting and architecture do not function on intervals of one.

The intervals and their weighting is really important to my writing work, which is how I make a living, so I apologise for not just publishing the code. That feels shitty of me. I don't want it to look like a black box filled with snake oil. It's just that for a writer, you don't really have much more than your voice.

I will, though, happily share it with anyone genuinely interested, in a reasonable way - hit me up. If this is worth pursuing, I would love to do that. Because I'm very much at the point where it's beyond me, now.

Email is in my Twitter - [@gabriel666smith](https://twitter.com/gabriel666smith).

---

*An experimental approach to language modeling using Fibonacci intervals in text analysis*
