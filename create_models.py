#!/usr/bin/env python3
import re
from collections import Counter
from fibonnaci_syllables import (
    fibonacci_sequence_unique, 
    best_syllable_split, 
    generate_fibonacci_bidirectional_multi
)


def text_to_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    return [word for word in words if word]


def fibonacci_sequence_unique_no_pos1(max_val: int) -> list[int]:
    fib = [2, 3]
    while fib[-1] < max_val:
        fib.append(fib[-1] + fib[-2])
    return [f for f in fib if f <= max_val]


def create_fibonacci_bidirectional_word_model(words, max_distance=200):
    print(f"📊 Building bidirectional WORD model from {len(words)} words...")
    
    forward_model = {}
    backward_model = {}
    fib_distances = fibonacci_sequence_unique_no_pos1(max_distance)
    
    print("🔮 Building forward word predictions...")
    for pos in range(len(words)):
        current_word = words[pos]
        
        for fib_distance in fib_distances:
            future_pos = pos + fib_distance
            if future_pos < len(words):
                future_word = words[future_pos]
                
                if current_word not in forward_model:
                    forward_model[current_word] = {}
                if fib_distance not in forward_model[current_word]:
                    forward_model[current_word][fib_distance] = Counter()
                
                forward_model[current_word][fib_distance][future_word] += 1
        
        if pos % 50000 == 0:
            print(f"  Forward: Processed {pos} words...")
    
    print("🔙 Building backward word predictions...")
    for pos in range(len(words)):
        current_word = words[pos]
        
        for fib_distance in fib_distances:
            past_pos = pos - fib_distance
            if past_pos >= 0:
                past_word = words[past_pos]
                
                if current_word not in backward_model:
                    backward_model[current_word] = {}
                if fib_distance not in backward_model[current_word]:
                    backward_model[current_word][fib_distance] = Counter()
                
                backward_model[current_word][fib_distance][past_word] += 1
        
        if pos % 50000 == 0:
            print(f"  Backward: Processed {pos} words...")
    
    print(f"✅ Forward word model: {len(forward_model)} unique words")
    print(f"✅ Backward word model: {len(backward_model)} unique words")
    
    return {'forward': forward_model, 'backward': backward_model}


def generate_fibonacci_bidirectional_words(word_models, start_word, start_pos, max_pos):
    fib_distances = fibonacci_sequence_unique_no_pos1(max_pos - start_pos)
    generated = {}
    analysis_data = {}
    
    forward_model = word_models['forward']
    backward_model = word_models['backward']
    
    for fib_dist in fib_distances:
        target_pos = start_pos + fib_dist
        if target_pos <= max_pos:
            forward_candidates = {}
            if start_word in forward_model and fib_dist in forward_model[start_word]:
                counts = forward_model[start_word][fib_dist]
                total = sum(counts.values())
                for word, count in counts.items():
                    forward_candidates[word] = count / total
            
            valid_candidates = {}
            for candidate_word, forward_prob in forward_candidates.items():
                backward_prob = 0.0
                if candidate_word in backward_model and fib_dist in backward_model[candidate_word]:
                    back_counts = backward_model[candidate_word][fib_dist]
                    back_total = sum(back_counts.values())
                    if start_word in back_counts:
                        backward_prob = back_counts[start_word] / back_total
                
                if backward_prob > 0:
                    combined_score = forward_prob * backward_prob
                    valid_candidates[candidate_word] = (forward_prob, backward_prob, combined_score)
            
            if valid_candidates:
                sorted_candidates = sorted(
                    [(word, forward, backward, combined) for word, (forward, backward, combined) in valid_candidates.items()],
                    key=lambda x: x[3], reverse=True
                )
                
                analysis_data[target_pos] = {
                    'all_candidates': sorted_candidates,
                    'from_seed': start_word,
                    'fib_distance': fib_dist
                }
                
                best_word = sorted_candidates[0][0]
                forward_prob, backward_prob, combined_score = sorted_candidates[0][1:]
                generated[target_pos] = (best_word, forward_prob, backward_prob, combined_score)
        
        target_pos = start_pos - fib_dist
        if target_pos >= 1:
            backward_candidates = {}
            if start_word in backward_model and fib_dist in backward_model[start_word]:
                counts = backward_model[start_word][fib_dist]
                total = sum(counts.values())
                for word, count in counts.items():
                    backward_candidates[word] = count / total
            
            valid_candidates = {}
            for candidate_word, backward_prob in backward_candidates.items():
                forward_prob = 0.0
                if candidate_word in forward_model and fib_dist in forward_model[candidate_word]:
                    forward_counts = forward_model[candidate_word][fib_dist]
                    forward_total = sum(forward_counts.values())
                    if start_word in forward_counts:
                        forward_prob = forward_counts[start_word] / forward_total
                
                if forward_prob > 0:
                    combined_score = forward_prob * backward_prob
                    valid_candidates[candidate_word] = (forward_prob, backward_prob, combined_score)
            
            if valid_candidates:
                sorted_candidates = sorted(
                    [(word, forward, backward, combined) for word, (forward, backward, combined) in valid_candidates.items()],
                    key=lambda x: x[3], reverse=True
                )
                
                analysis_data[target_pos] = {
                    'all_candidates': sorted_candidates,
                    'from_seed': start_word,
                    'fib_distance': -fib_dist
                }
                
                best_word = sorted_candidates[0][0]
                forward_prob, backward_prob, combined_score = sorted_candidates[0][1:]
                generated[target_pos] = (best_word, forward_prob, backward_prob, combined_score)
    
    return generated, analysis_data


def syllable_word_similarity(syllable, word):
    word_syllables = best_syllable_split(word)
    
    if syllable in word_syllables:
        return 1.0
    
    if syllable in word:
        return 0.7
    
    if len(syllable) >= 2 and len(word) >= 2:
        if syllable[:2] == word[:2]:
            return 0.3
        if syllable[-2:] == word[-2:]:
            return 0.2
    
    return 0.0


def generate_fibonacci_bidirectional_multi_words(word_models, seed_words, length=20, verbose=True):
    if verbose:
        print(f"🔄 Bidirectional multi-calc word generation: {length} positions")
        print(f"🌱 Full word seed: {seed_words}")
    
    sequence = {}
    all_analysis_data = {}
    max_pos = length
    
    for i, word in enumerate(seed_words):
        pos = i + 1
        if pos <= max_pos:
            sequence[pos] = (word, 1.0, 1.0, 1.0)
            all_analysis_data[pos] = {
                'all_candidates': [(word, 1.0, 1.0, 1.0)],
                'from_seed': 'SEED',
                'fib_distance': 0
            }
            if verbose:
                print(f"🌱 Seed pos {pos}: '{word}'")
    
    for i, seed_word in enumerate(seed_words):
        start_pos = i + 1
        if start_pos <= max_pos:
            if verbose:
                print(f"\n🔄 Bidirectional word gen from position {start_pos} ('{seed_word}'):")
            gen, analysis_data = generate_fibonacci_bidirectional_words(word_models, seed_word, start_pos, max_pos)
            
            for pos, data in analysis_data.items():
                if pos not in all_analysis_data:
                    all_analysis_data[pos] = {'competing_options': []}
                if 'competing_options' not in all_analysis_data[pos]:
                    all_analysis_data[pos]['competing_options'] = []
                all_analysis_data[pos]['competing_options'].append(data)
            
            for pos in sorted(gen.keys()):
                word, forward_prob, backward_prob, combined_score = gen[pos]
                if pos in sequence:
                    existing_word, existing_forward, existing_backward, existing_score = sequence[pos]
                    if existing_score == 1.0:
                        if verbose:
                            print(f"  Pos {pos}: '{word}' (F:{forward_prob:.1%} B:{backward_prob:.1%} C:{combined_score:.3f}) [keeps SEED '{existing_word}']")
                    elif combined_score > existing_score:
                        if verbose:
                            print(f"  Pos {pos}: '{word}' (F:{forward_prob:.1%} B:{backward_prob:.1%} C:{combined_score:.3f}) [REPLACES '{existing_word}' (C:{existing_score:.3f})")
                        sequence[pos] = (word, forward_prob, backward_prob, combined_score)
                    else:
                        if verbose:
                            print(f"  Pos {pos}: '{word}' (F:{forward_prob:.1%} B:{backward_prob:.1%} C:{combined_score:.3f}) [keeps '{existing_word}' (C:{existing_score:.3f})")
                else:
                    if verbose:
                        print(f"  Pos {pos}: '{word}' (F:{forward_prob:.1%} B:{backward_prob:.1%} C:{combined_score:.3f}) [FILLS GAP]")
                    sequence[pos] = (word, forward_prob, backward_prob, combined_score)
    
    result = []
    if verbose:
        print(f"\n✨ Final word sequence:")
    for pos in range(1, max_pos + 1):
        if pos in sequence:
            word = sequence[pos][0]
            result.append(word)
            if verbose:
                print(f"  {pos}: {word}")
        else:
            result.append("_")
            if verbose:
                print(f"  {pos}: _ (gap)")
    
    if verbose:
        final_filled = [w for w in result if w != "_"]
        print(f"Final filled words: {' '.join(final_filled)}")
    
    return result, all_analysis_data


def generate_fibonacci_diffusion_words(word_models, seed_words, length=20, diffusion_steps=3, verbose=True):
    if verbose:
        print(f"🌊 WORD DIFFUSION GENERATION: {diffusion_steps} steps, {length} positions")
        print(f"🌱 Initial word seed: {seed_words}")
    
    current_sequence = {}
    all_analysis_data = {}
    
    for i, word in enumerate(seed_words):
        pos = i + 1
        if pos <= length:
            current_sequence[pos] = (word, 1.0, 0)
            all_analysis_data[pos] = {
                'step_history': [{'step': 0, 'source': 'SEED', 'candidates': [(word, 1.0, 1.0, 1.0)], 'chosen': word}]
            }
    
    for step in range(diffusion_steps):
        if verbose:
            print(f"\n🌊 WORD DIFFUSION STEP {step + 1}/{diffusion_steps}")
        
        starting_points = []
        for pos in sorted(current_sequence.keys()):
            word, weight, _ = current_sequence[pos]
            starting_points.append((pos, word, weight))
        
        step_proposals = {}
        step_analysis = {}
        
        for start_pos, start_word, start_weight in starting_points:
            if verbose:
                print(f"  🔄 Word gen from pos {start_pos} ('{start_word}', w:{start_weight:.3f})")
            
            gen, gen_analysis = generate_fibonacci_bidirectional_words(word_models, start_word, start_pos, length)
            
            for pos, analysis in gen_analysis.items():
                if pos not in step_analysis:
                    step_analysis[pos] = {'source_analyses': []}
                
                analysis['source_pos'] = start_pos
                analysis['source_word'] = start_word
                analysis['source_weight'] = start_weight
                analysis['step'] = step + 1
                step_analysis[pos]['source_analyses'].append(analysis)
            
            for pos, (word, forward_prob, backward_prob, combined_score) in gen.items():
                weighted_score = combined_score * start_weight
                
                if pos not in step_proposals:
                    step_proposals[pos] = []
                step_proposals[pos].append((word, weighted_score, start_pos, start_weight, forward_prob, backward_prob, combined_score))
        
        for pos in step_proposals:
            proposals = step_proposals[pos]
            best_proposal = max(proposals, key=lambda x: x[1])
            best_word, best_score, source_pos, source_weight, forward_prob, backward_prob, combined_score = best_proposal
            
            step_candidates = []
            for word, w_score, s_pos, s_weight, f_prob, b_prob, c_score in proposals:
                step_candidates.append((word, f_prob, b_prob, c_score))
            step_candidates.sort(key=lambda x: x[3], reverse=True)
            
            if pos not in all_analysis_data:
                all_analysis_data[pos] = {'step_history': []}
            
            all_analysis_data[pos]['step_history'].append({
                'step': step + 1,
                'source': f"pos_{source_pos}",
                'candidates': step_candidates,
                'chosen': best_word if pos not in current_sequence or current_sequence[pos][2] != 0 else current_sequence[pos][0]
            })
            
            if pos in current_sequence:
                existing_word, existing_weight, existing_step = current_sequence[pos]
                
                if existing_step == 0:
                    if verbose:
                        print(f"    Pos {pos}: keeps SEED '{existing_word}' vs '{best_word}'")
                elif best_score > existing_weight:
                    if verbose:
                        print(f"    Pos {pos}: '{best_word}' (w:{best_score:.3f}) REPLACES '{existing_word}' (w:{existing_weight:.3f})")
                    current_sequence[pos] = (best_word, best_score, step + 1)
                    all_analysis_data[pos]['step_history'][-1]['chosen'] = best_word
                else:
                    if verbose:
                        print(f"    Pos {pos}: keeps '{existing_word}' (w:{existing_weight:.3f}) vs '{best_word}' (w:{best_score:.3f})")
            else:
                if verbose:
                    print(f"    Pos {pos}: '{best_word}' (w:{best_score:.3f}) FILLS GAP")
                current_sequence[pos] = (best_word, best_score, step + 1)
                all_analysis_data[pos]['step_history'][-1]['chosen'] = best_word
    
    result = []
    if verbose:
        print(f"\n✨ FINAL DIFFUSED WORD SEQUENCE:")
    for pos in range(1, length + 1):
        if pos in current_sequence:
            word, weight, step = current_sequence[pos]
            result.append(word)
            if verbose:
                print(f"  {pos:2d}: {word} (w:{weight:.3f}, step:{step})")
        else:
            result.append("_")
            if verbose:
                print(f"  {pos:2d}: _ (gap)")
    
    return result, all_analysis_data


def generate_fibonacci_dual_level(syllable_models, word_models, seed_words, length=20):
    seed_syllables = []
    for word in seed_words:
        seed_syllables.extend(best_syllable_split(word))
    
    if len(seed_syllables) <= 5:
        effective_length = max(length, len(seed_syllables) + 20)
    elif len(seed_syllables) <= 15:
        effective_length = max(length, len(seed_syllables) + 15)
    else:
        effective_length = max(length, len(seed_syllables) + 12)
    
    effective_length = max(effective_length, 25)
    
    print(f"🔄 DUAL-LEVEL Fibonacci generation: {effective_length} positions")
    print(f"🌱 Seed words: {seed_words}")
    print(f"🌱 Seed syllables: {seed_syllables} ({len(seed_syllables)} syllables)")
    print(f"🎯 Forcing extension from {len(seed_syllables)} to {effective_length} positions")
    
    print("\n📝 Generating syllable sequence...")
    syllable_result = generate_fibonacci_bidirectional_multi(syllable_models, seed_syllables, effective_length, verbose=False)
    
    print("\n📖 Generating word sequence...")
    word_sequence = {}
    max_word_pos = effective_length // 2 + len(seed_words)
    
    for i, word in enumerate(seed_words):
        pos = i + 1
        word_sequence[pos] = (word, 1.0, 1.0, 1.0)
    
    for i, seed_word in enumerate(seed_words):
        start_pos = i + 1
        if start_pos <= max_word_pos:
            word_gen, _ = generate_fibonacci_bidirectional_words(word_models, seed_word, start_pos, max_word_pos)
            
            for pos in sorted(word_gen.keys()):
                word, forward_prob, backward_prob, combined_score = word_gen[pos]
                if pos in word_sequence:
                    existing_word, existing_forward, existing_backward, existing_score = word_sequence[pos]
                    if existing_score == 1.0:
                        continue
                    elif combined_score > existing_score:
                        word_sequence[pos] = (word, forward_prob, backward_prob, combined_score)
                else:
                    word_sequence[pos] = (word, forward_prob, backward_prob, combined_score)
    
    print("\n🔗 Aligning syllables with words...")
    final_result = []
    
    word_list = []
    for pos in range(1, max_word_pos + 1):
        if pos in word_sequence:
            word_list.append(word_sequence[pos][0])
        else:
            word_list.append(None)
    
    clean_syllables = [s for s in syllable_result if s != '_']
    clean_words = [w for w in word_list if w]
    
    syllable_to_word = {}
    used_words = set()
    
    for i, syl in enumerate(syllable_result):
        if syl != '_':
            best_word = None
            best_similarity = 0.0
            
            for word in word_list:
                if word and word not in used_words:
                    similarity = syllable_word_similarity(syl, word)
                    if similarity > best_similarity:
                        best_similarity = similarity
                        best_word = word
            
            if best_word and best_similarity > 0.3:
                syllable_to_word[i] = best_word
                used_words.add(best_word)
                final_result.append(best_word)
            else:
                final_result.append(syl)
    
    print("\n" + "="*70)
    print("🎯 DUAL-LEVEL GENERATION RESULTS")
    print("="*70)
    
    print(f"\n📝 SYLLABLE VERSION ({len(clean_syllables)} syllables):")
    print(f"   {' '.join(clean_syllables)}")
    
    print(f"\n📖 WORD-ENHANCED VERSION ({len(final_result)} elements):")
    print(f"   {' '.join(final_result)}")
    
    if syllable_to_word:
        print(f"\n🔗 ALIGNMENTS ({len(syllable_to_word)} syllables → words):")
        for i, word in syllable_to_word.items():
            syl = syllable_result[i] if i < len(syllable_result) else "?"
            similarity = 0
            if syl != "?" and word in clean_words:
                similarity = syllable_word_similarity(syl, word)
            print(f"   '{syl}' → '{word}' (similarity: {similarity:.1f})")
    
    print("="*70)
    
    return {
        'syllable_version': ' '.join(clean_syllables),
        'word_enhanced_version': ' '.join(final_result),
        'alignments': syllable_to_word
    }


def run_dual_interactive_mode(syllable_model, word_model):
    print("\n🎮 Dual-Level Interactive Mode")
    print("Commands: 'quit' to exit, or enter words/phrases")
    print("Generate: syllable-only AND dual-level (syllables+words) for comparison")
    
    while True:
        user_input = input("\n> ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        if user_input:
            input_words = re.findall(r'\b[a-zA-Z]+\b', user_input.lower())
            if input_words:
                print(f"\n💬 Input words: {input_words}")
                
                seed_syllables = []
                for word in input_words:
                    seed_syllables.extend(best_syllable_split(word))
                print(f"💬 Input syllables: {seed_syllables}")
                
                print("\n🔸 Syllable-only generation:")
                syl_result = generate_fibonacci_bidirectional_multi(syllable_model, seed_syllables, length=12)
                syl_filled = [s for s in syl_result if s != '_']
                print(f"   {' '.join(syl_filled)}")
                
                print("\n🔸 Dual-level generation (syllables + words):")
                dual_result = generate_fibonacci_dual_level(syllable_model, word_model, input_words, length=12)
                print(f"   {' '.join(dual_result)}")
            else:
                print("❌ No valid words found")

def train_word_model(text_file, max_distance=200):
    words = text_to_words(text_file)
    return create_fibonacci_bidirectional_word_model(words, max_distance)

def test_dual_generation(syllable_model, word_model, test_phrases):
    print('🚀 DUAL-LEVEL FIBONACCI COMPARISON TESTS')
    print('='*60)

    for words in test_phrases:
        print(f'\n📝 Testing: {" ".join(words)}')
        
        syllables = []
        for word in words:
            syllables.extend(best_syllable_split(word))
        print(f'🌱 Syllables: {syllables}')
        
        print('\n🔸 Syllable-only result:')
        syl_result = generate_fibonacci_bidirectional_multi(syllable_model, syllables, length=12)
        syl_clean = [s for s in syl_result if s != '_']
        print(f'   {" ".join(syl_clean)}')
        
        print('\n🔸 Dual-level result (syllables + words):')
        dual_result = generate_fibonacci_dual_level(syllable_model, word_model, words, length=12)
        print(f'   {" ".join(dual_result)}')
        print('\n' + '-'*50)

if __name__ == '__main__':
    import pickle

    input_text_file = 'test.txt'
    output_model_file = 'fibonacci_word_model.pkl'

    print(f"🚀 Starting word model training from: {input_text_file}")
    word_model = train_word_model(input_text_file, max_distance=200)

    print(f"💾 Saving trained word model to: {output_model_file}")
    with open(output_model_file, 'wb') as f:
        pickle.dump(word_model, f)

    print("✅ Word model training and saving complete.")
