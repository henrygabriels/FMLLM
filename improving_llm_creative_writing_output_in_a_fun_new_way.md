# A Small Experiment in Improving LLM Creative Writing Using Fibonacci Word Embeddings

I took a small corpus of literary fiction (~700k words) and created a model of which words are most likely to appear at *Fibonacci intervals* to each other — not adjacent, but at specific distances apart.

From this, I could take a prompt and generate 50 words that may or may not be linked to the prompt.  
I appended these to prompts like:

- “Write a story about a dog”  
- “Write a story about love”  
- “Write a story about grief”  

In this format:

[You may wish to use the following words in your story, either as inspiration or for direct usage. The choice is yours: {fib_words}]


I used **Mistral’s Nemo** to generate the stories (cheap + strong at roleplay on OpenRouter) and **Gemini Flash 2.0** to assess them (cheap + anecdotal sense that it’s “tough” in evaluation).

I generated **300 stories** (100 for each topic, with and without appended words).  
It’s a small dataset; I’m broke.  

The judging criteria were adapted from [EQ Bench’s creative writing benchmarks](https://eqbench.com/about.html#creative-writing-v3).  
Results were surprising: significant improvements with Fibonacci embeddings.

> **Note**: I don’t think AIs “know” what good writing is. Using them to benchmark creative writing is absurd. But still, the comparison is useful.

---

## Results

| Benchmark                 | No extra words | Random words (Δ) | Fibonacci words (Δ) |
|----------------------------|----------------|------------------|---------------------|
| Authenticity of character  | 2.96           | 3.14 (+6.13%)    | 3.64 (+23.19%)      |
| Originality of voice       | 2.37           | 2.99 (+26.16%)   | 3.40 (+43.63%)      |
| Quality of prose           | 4.32           | 4.48 (+3.82%)    | 4.77 (+10.36%)      |
| Artistic coherence         | 5.06           | 4.79 (−5.18%)    | 4.72 (−6.78%)       |
| Quality of world created   | 4.13           | 4.46 (+8.10%)    | 5.08 (+23.02%)      |
| **Overall Quality**        | 3.44           | 3.73 (+8.35%)    | 4.07 (+18.33%)      |

---

## Assessment Prompt

Please carefully read the following story and provide a detailed, harsh if necessary, honest analysis of its literary merits, followed by numerical ratings. Use all your knowledge of literary fiction to make this assessment. Be a nuanced and artistic critic. See merits and flaws with equal honesty.

Story:
{story}

First, provide your reasoning and analysis of the story's strengths and weaknesses across the various literary dimensions. Then, after your analysis, IT IS CRITICAL THAT YOU CORRECTLY FORMAT your numerical ratings using the exact format specified below for each category, following the separator "***". Format your response exactly like this:

Avoidance of cliches: [score/10]
Character authenticity, providing unique insight: [score/10]
Originality of voice: [score/10]
Quality of prose: [score/10]
Artistic coherence in plotting: [score/10]
The world created by the prose: [score/10]
Overall literary quality: [score/10]

---

## Story Samples

Here are some side-by-side examples (all from the “grief” prompt).  
I haven’t cherry-picked; these just stood out.

- **The Echoes of Absence** *(No appended words)*  
  *(Excerpt omitted here for brevity — see full version above in repo)*  

- **The Lighthouse Keeper** *(Random words appended)*  
  *(Excerpt omitted)*  

- **The Unending Reel** *(Fibonacci words appended)*  
  *(Excerpt omitted)*  

---

## How Easy Would This Be to Automate?

The process is extremely lightweight. A company with existing infrastructure could implement this in a few steps:

1. **Precompute embeddings**  
   - Take any large text corpus (fiction, user-generated text, etc.).  
   - Build a lookup table of words likely to co-occur at Fibonacci intervals.  
   - This is a one-time cost, not computationally heavy.  

2. **Augment prompts**  
   - When a user sends a creative-writing request, fetch ~50 Fibonacci-related words from the lookup table.  
   - Append them in the “optional words” format.  

3. **Model-agnostic**  
   - Works with any text generation model — no fine-tuning needed.  
   - Zero modification of the base model.  

4. **Assessment pipeline**  
   - Companies could use LLM-based judges, human raters, or hybrid methods.  
   - Scaling up would give far more reliable benchmarks than my tiny dataset.  

Essentially, the whole pipeline is a **cheap prompt add-on**, not a major research lift.  
A company like Anthropic, OpenAI, or even a fanfiction site could run this at scale without changing their models at all. I find it useful :-)
