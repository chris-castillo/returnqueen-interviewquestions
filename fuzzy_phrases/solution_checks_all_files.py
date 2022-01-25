import json

def phrasel_search(P, Queries):
    # split each to individual words
    p_split = [p.split() for p in P]
    q_split = [q.split() for q in Queries]

    ans_split = []

    # iterate over each query
    for query in q_split:
        # start list per query
        ans_split.append([])

        # start phrase index per query to sort resulting list
        phrase_order_in_query = []

        for specific_phrase in p_split:
            # find all occurrences of first word of phrase in query
            # from https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
            occurrence_indices = [i for i, x in enumerate(query) if x == specific_phrase[0]]

            # if we found at least 1, proceed
            if len(occurrence_indices) > 0:

                # iterate over all these occurrences (there may be more than 1!)
                for occurrence_index in occurrence_indices:

                    current_query_index = 0
                    # we only get one extra word
                    used_one_extra_word = False
                    # this will be the final phrase if we are successful
                    total_phrase_in_query = []

                    # now iterate through this phrase
                    for phrase_word in specific_phrase:
                        # standard, check if query[start + i] == phrase[i]
                        if query[occurrence_index+current_query_index] == phrase_word:
                            total_phrase_in_query.append(phrase_word)
                            current_query_index += 1
                            pass
                        # this handles the one extra word
                        # first check we don't index out of bounds
                        elif len(query) > occurrence_index+current_query_index + 1:
                            # look ahead, if query[i + 1] == phrase[i], then store the extra word and continue
                            if query[occurrence_index+current_query_index + 1] == phrase_word and not used_one_extra_word:
                                total_phrase_in_query.append(query[occurrence_index + current_query_index])
                                total_phrase_in_query.append(query[occurrence_index + current_query_index + 1])
                                current_query_index += 1
                                used_one_extra_word = True
                                current_query_index += 1
                        # at any point if the above fails, escape loop
                        else:
                            break

                    # make sure the count of words checked matches the length of the phrase
                    if current_query_index == len(specific_phrase) or current_query_index == len(specific_phrase) + 1:
                        # the lengths match, so add it
                        ans_split[-1].append(total_phrase_in_query)
                        phrase_order_in_query.append(occurrence_index)

        # we want to sort all phrase occurrences in this query by the order in which they occur in the query
        # (to match the order in the solution)
        # from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        ans_split[-1] = [x for _, x in sorted(zip(phrase_order_in_query, ans_split[-1]))]

    # every word is its own element in the list of lists
    # need to collapse down to string with spaces in between each word
    ans = []
    for ans_per_query in ans_split:
        ans.append([])
        for an in ans_per_query:
            ans[-1].append(' '.join(an))    

    return ans

if __name__ == "__main__":
    for file in ['sample.json', '20_points.json', '30_points.json', '50_points.json', '20_points_with_empty.json']:
        with open(file, 'r') as f:
            sample_data = json.loads(f.read())
            P, Queries = sample_data['phrases'], sample_data['queries']
            returned_ans = phrasel_search(P, Queries)

            if returned_ans == sample_data['solution']:
                print("TEST PASSED for file: " + file)
            else:
                print("TEST FAILED for file: " + file)

# EXPECTED OUTPUT:
# TEST PASSED for file: sample.json
# TEST PASSED for file: 20_points.json
# TEST PASSED for file: 30_points.json
# TEST PASSED for file: 50_points.json
# TEST FAILED for file: 20_points_with_empty.json