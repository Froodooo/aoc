from copy import deepcopy


def run_a(input_file):
    options = {'part': 'a'}
    players = _read(input_file)
    winner = _play_game(players, options)
    return _winning_score(players, winner)


def run_b(input_file):
    options = {'part': 'b'}
    players = _read(input_file)
    winner = _play_game(players, options)
    return _winning_score(players, winner)


def _play_game(players, options):
    finished = False
    rounds = []

    while not finished:
        finished, winner = _play_round(players, rounds, options)

    return winner


def _play_round(players, rounds, options):
    part = options['part']

    if part == 'b' and _is_infinite_game(players, rounds):
        return True, 1
    else:
        rounds.append(tuple(deepcopy(players).values()))

    cards_on_top = [(player_id, cards.pop(0))
                    for player_id, cards in players.items()]

    if part == 'b' and _is_recursive_game(dict(cards_on_top), players):
        players_copy = _players_copy(deepcopy(players), dict(cards_on_top))
        winner = _play_game(players_copy, options)
    else:
        winner, _ = sorted(cards_on_top, key=lambda x: x[1], reverse=True)[0]

    sorted_cards_on_top = _sort_cards_on_top(cards_on_top, winner, part)
    players[winner] = players[winner] + sorted_cards_on_top

    return _is_finished(players)


def _sort_cards_on_top(cards_on_top, winner, part):
    if part == 'a':
        return sorted([card for (_, card) in cards_on_top], reverse=True)
    elif part == 'b':
        cards_on_top = dict(cards_on_top)
        winning_card = cards_on_top[winner]
        rest_cards = list(
            dict(filter(lambda cards: cards[0] != winner, cards_on_top.items())).values())
        rest_cards.insert(0, winning_card)
        return rest_cards


def _players_copy(players, cards_on_top):
    return {player_id: cards[:cards_on_top[player_id]]
            for player_id, cards in players.items()}


def _is_recursive_game(cards_on_top, players):
    number_of_players = sum([1 if len(
        players[player_id]) >= cards_on_top[player_id] else 0 for player_id in players.keys()])
    return number_of_players == len(players)


def _is_infinite_game(players, rounds):
    return tuple(players.values()) in rounds


def _is_finished(players):
    total_players = len(players)
    players_with_empty_deck = sum(
        [1 if len(cards) == 0 else 0 for cards in players.values()])

    if total_players == players_with_empty_deck + 1:
        winner, _ = list(filter(lambda player: len(
            player[1]) > 0, players.items()))[0]
        return True, winner

    return False, None


def _winning_score(players, winner):
    cards = players[winner]

    return sum([card * (index + 1) for index, card in enumerate(reversed(cards))])


def _read(file_name):
    with open(file_name) as f:
        players = f.read().split('\n\n')
        players = {int(player.split('\n')[0].split()[1][-2]):
                   [int(card) for card in player.split('\n')[1:]]
                   for player in players}

    return players


def solve():
    input_file = 'day22/22.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
