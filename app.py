from flask import Flask, redirect, render_template, url_for, request, redirect, jsonify
# from datetime import datetime
import pandas as pd
# import random
import os
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

app = Flask(__name__)





words = ['aargh', 'abaca', 'abaci', 'aback', 'abaft', 'abase', 'abash', 'abate', 'abaya', 'abbey', 'abbot', 'abeam', 'abend', 'abets', 'abhor', 'abide', 'abled', 'abler', 'abode', 'abort', 
'about', 'above', 'absit', 'abuse', 'abuts', 'abuzz', 'abyss', 'ached', 'aches', 'achoo', 'acids', 'acing', 'acked', 'ackee', 'acmes', 'acned', 'acnes', 'acorn', 'acres', 'acrid', 
'acted', 'actor', 'acute', 'adage', 'adapt', 'added', 'adder', 'addle', 'adept', 'adieu', 'adios', 'adits', 'adlib', 'adman', 'admen', 'admin', 'admit', 'admix', 'adobe', 'adobo', 
'adopt', 'adore', 'adorn', 'adult', 'adzes', 'aegis', 'aeons', 'aerie', 'affix', 'afire', 'afoot', 'afore', 'afoul', 'after', 'again', 'agape', 'agars', 'agate', 'agave', 'agent', 
'agile', 'aging', 'agley', 'aglow', 'agone', 'agony', 'agora', 'agree', 'agues', 'ahead', 'ahhhh', 'ahold', 'ahoys', 'aided', 'aider', 'aides', 'ailed', 'aimed', 'aimer', 'aired', 
'airer', 'aisle', 'aitch', 'ajuga', 'alack', 'alarm', 'album', 'alder', 'aleck', 'aleph', 'alert', 'algae', 'algal', 'algin', 'alias', 'alibi', 'alien', 'align', 'alike', 'alive', 
'alkyd', 'alkyl', 'allay', 'alley', 'allot', 'allow', 'alloy', 'allyl', 'aloes', 'aloft', 'aloha', 'alone', 'along', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'altos', 'alums', 
'alway', 'amahs', 'amass', 'amaze', 'amber', 'ambit', 'amble', 'ambos', 'ameba', 'amend', 'amens', 'amide', 'amigo', 'amine', 'amino', 'amiss', 'amity', 'amnio', 'among', 'amour', 
'amped', 'ample', 'amply', 'amuck', 'amuse', 'amyls', 'ancho', 'anded', 'anent', 'angel', 'anger', 'angle', 'angry', 'angst', 'anile', 'anima', 'anime', 'anion', 'anise', 'ankhs', 
'ankle', 'annas', 'annex', 'annoy', 'annul', 'annum', 'anode', 'anole', 'anted', 'antes', 'antic', 'antis', 'antsy', 'anvil', 'aorta', 'apace', 'apart', 'apers', 'aphid', 'aphis', 
'apian', 'aping', 'apish', 'apnea', 'aport', 'apple', 'apply', 'apron', 'apses', 'apsos', 'apter', 'aptly', 'aquae', 'aquas', 'arbor', 'arced', 'ardor', 'areal', 'areas', 'areca', 
'arena', 'argon', 'argot', 'argue', 'argus', 'arias', 'arils', 'arise', 'arity', 'armed', 'armor', 'aroma', 'arose', 'arras', 'array', 'arrow', 'arson', 'artsy', 'arums', 'asana', 
'ascot', 'ashen', 'ashes', 'aside', 'asked', 'asker', 'askew', 'aspen', 'aspic', 'assai', 'assay', 'assed', 'asses', 'asset', 'aster', 'astro', 'asura', 'atilt', 'atlas', 'atman', 
'atoll', 'atoms', 'atone', 'atopy', 'atria', 'attar', 'attic', 'audio', 'audit', 'auger', 'aught', 'augur', 'aunts', 'aunty', 'aural', 'auras', 'auric', 'autos', 'auxin', 'avail', 
'avant', 'avast', 'avers', 'avert', 'avian', 'avoid', 'avows', 'await', 'awake', 'award', 'aware', 'awash', 'aways', 'awful', 'awing', 'awoke', 'axels', 'axial', 'axils', 'axing', 
'axiom', 'axion', 'axled', 'axles', 'axman', 'axmen', 'axons', 'ayins', 'azide', 'azine', 'azoic', 'azole', 'azure', 'babes', 'babka', 'backs', 'bacon', 'baddy', 'badge', 'badly', 
'bagel', 'baggy', 'bahts', 'bails', 'bairn', 'baits', 'baize', 'baked', 'baker', 'bakes', 'balds', 'baldy', 'baler', 'bales', 'balks', 'balky', 'balls', 'bally', 'balms', 'balmy', 
'balsa', 'banal', 'bands', 'bandy', 'banes', 'bangs', 'banjo', 'banks', 'banns', 'barbs', 'bards', 'barer', 'bares', 'barfs', 'barfy', 'barge', 'baric', 'barks', 'barky', 'barms', 
'barmy', 'barns', 'baron', 'barre', 'basal', 'based', 'baser', 'bases', 'basic', 'basil', 'basin', 'basis', 'basks', 'bassi', 'basso', 'bassy', 'baste', 'batch', 'bated', 'bates', 
'bathe', 'baths', 'batik', 'baton', 'batts', 'batty', 'bauds', 'baulk', 'bawdy', 'bawls', 'bayou', 'bazar', 'beach', 'beads', 'beady', 'beaks', 'beaky', 'beams', 'beamy', 'beano', 
'beans', 'beard', 'bears', 'beast', 'beats', 'beaus', 'beaut', 'beaux', 'bebop', 'becks', 'bedew', 'bedim', 'beech', 'beefs', 'beefy', 'beeps', 'beers', 'beery', 'beets', 'befit', 
'befog', 'began', 'begat', 'beget', 'begin', 'begot', 'begun', 'beige', 'being', 'belay', 'belch', 'belie', 'belle', 'belli', 'bells', 'belly', 'below', 'belts', 'bench', 'bends', 
'bendy', 'bento', 'bents', 'beret', 'bergs', 'berms', 'berry', 'berth', 'beset', 'besot', 'bests', 'betas', 'betel', 'beths', 'betta', 'bevel', 'bezel', 'bhaji', 'bhang', 'bhoys', 
'bibbs', 'bible', 'bicep', 'biddy', 'bided', 'bider', 'bides', 'biers', 'biffs', 'biffy', 'biggy', 'bight', 'bigly', 'bigot', 'bijou', 'biked', 'biker', 'bikes', 'biles', 'bilge', 
'bilgy', 'bilks', 'bills', 'billy', 'bimbo', 'bindi', 'binge', 'bingo', 'biome', 'biota', 'biped', 'bipod', 'birch', 'birds', 'birth', 'bison', 'bitch', 'biter', 'bites', 'bitsy', 
'bitty', 'blabs', 'black', 'blade', 'blahs', 'blame', 'bland', 'blank', 'blare', 'blase', 'blash', 'blast', 'blats', 'blaze', 'bleak', 'blear', 'bleat', 'blebs', 'bleed', 'bleep', 
'blend', 'bless', 'blest', 'blimp', 'blind', 'blini', 'blink', 'blips', 'bliss', 'blitz', 'bloat', 'blobs', 'block', 'blocs', 'blogs', 'bloke', 'blond', 'blood', 'bloom', 'bloop', 
'blots', 'blown', 'blows', 'blowy', 'bluer', 'blues', 'bluey', 'bluff', 'blunt', 'blurb', 'blurs', 'blurt', 'blush', 'board', 'boars', 'boast', 'boats', 'bobby', 'bocce', 'bocci', 
'boche', 'bocks', 'boded', 'bodge', 'boffo', 'boffs', 'bogey', 'boggy', 'bogie', 'bogus', 'boils', 'bolas', 'boles', 'bolls', 'bolos', 'bolts', 'bolus', 'bombe', 'bombs', 'bonds', 
'boned', 'boner', 'boney', 'bongo', 'bongs', 'bonks', 'bonne', 'bonny', 'bonus', 'boobs', 'booby', 'booed', 'books', 'booky', 'booms', 'boomy', 'boons', 'boors', 'boost', 'booth', 
'boots', 'booty', 'booze', 'boozy', 'boppy', 'borax', 'bored', 'borer', 'bores', 'boric', 'borne', 'boron', 'bosky', 'bosom', 'boson', 'bossa', 'bossy', 'bosun', 'botch', 'bough', 
'boule', 'bound', 'bouts', 'bowed', 'bowel', 'bower', 'bowie', 'bowls', 'boxed', 'boxer', 'boxes', 'boyar', 'boyos', 'bozos', 'brace', 'brack', 'bract', 'brads', 'braes', 'brags', 
'braid', 'brain', 'brake', 'brand', 'brans', 'brant', 'brash', 'brass', 'brats', 'brava', 'brave', 'bravo', 'brawl', 'brawn', 'brays', 'braze', 'bread', 'break', 'bream', 'breed', 
'brent', 'brews', 'briar', 'bribe', 'brick', 'bride', 'brief', 'brier', 'bries', 'brigs', 'brims', 'brine', 'bring', 'brink', 'briny', 'brisk', 'brits', 'broad', 'broch', 'broil', 
'broke', 'brome', 'bromo', 'bronc', 'bronx', 'brood', 'brook', 'broom', 'broth', 'brown', 'brows', 'bruin', 'bruit', 'brung', 'brunt', 'brush', 'brusk', 'brute', 'bubba', 'bucks', 
'buddy', 'budge', 'buena', 'bueno', 'buffa', 'buffo', 'buffs', 'buggy', 'bugle', 'build', 'built', 'bulbs', 'bulge', 'bulgy', 'bulks', 'bulky', 'bulla', 'bulls', 'bully', 'bumph', 
'bumpy', 'bunch', 'bunco', 'bunds', 'bundt', 'bungs', 'bunko', 'bunks', 'bunny', 'bunts', 'buoys', 'burbs', 'buret', 'burgs', 'burka', 'burls', 'burly', 'burns', 'burnt', 'burqa', 
'burro', 'burrs', 'burry', 'bursa', 'burst', 'busby', 'bused', 'buses', 'bushy', 'busks', 'busts', 'busty', 'butch', 'butte', 'butts', 'butyl', 'buxom', 'buyer', 'bwana', 'bylaw', 
'byres', 'bytes', 'byway', 'cabal', 'cabby', 'caber', 'cabin', 'cable', 'cacao', 'cache', 'cacti', 'caddy', 'cadet', 'cadge', 'cadre', 'cafes', 'caged', 'cages', 'cagey', 'cairn', 
'caked', 'cakes', 'cakey', 'calfs', 'calif', 'calix', 'calks', 'calla', 'calls', 'calms', 'calve', 'calyx', 'camel', 'cameo', 'campo', 'camps', 'canal', 'candy', 'caned', 'caner', 
'canes', 'canid', 'canna', 'canny', 'canoe', 'canon', 'canst', 'canto', 'cants', 'caped', 'caper', 'capes', 'capon', 'capos', 'caput', 'carat', 'carbo', 'carbs', 'cards', 'cared', 
'carer', 'cares', 'caret', 'cargo', 'carne', 'carny', 'carob', 'carol', 'carom', 'caron', 'carps', 'carpy', 'carry', 'carte', 'carts', 'carve', 'casas', 'cased', 'cases', 'casks', 
'caste', 'casts', 'casus', 'catch', 'cater', 'catty', 'caulk', 'cauls', 'cause', 'caved', 'caver', 'caves', 'cavil', 'cawed', 'cease', 'cecum', 'cedar', 'ceded', 'ceder', 'cedes', 
'ceili', 'ceils', 'celeb', 'cello', 'cells', 'celts', 'cento', 'cents', 'chads', 'chafe', 'chaff', 'chain', 'chair', 'chalk', 'champ', 'chana', 'chant', 'chaos', 'chaps', 'chard', 
'charm', 'chars', 'chart', 'chary', 'chase', 'chasm', 'chats', 'chaws', 'cheap', 'cheat', 'check', 'cheek', 'cheep', 'cheer', 'chemo', 'chert', 'chess', 'chest', 'chews', 'chewy', 
'chica', 'chick', 'chico', 'chide', 'chief', 'chiff', 'child', 'chile', 'chili', 'chill', 'chime', 'chimp', 'china', 'ching', 'chink', 'chino', 'chins', 'chips', 'chirp', 'chits', 
'chive', 'chock', 'choir', 'choke', 'chomp', 'choos', 'chops', 'chord', 'chore', 'chose', 'chows', 'chubs', 'chuck', 'chuff', 'chugs', 'chump', 'chums', 'chunk', 'churl', 'churn', 
'chute', 'cider', 'cigar', 'cilia', 'cills', 'cinch', 'circa', 'cirri', 'cisco', 'cited', 'cites', 'civet', 'civic', 'civil', 'civvy', 'clack', 'clade', 'clads', 'claim', 'clamp', 
'clams', 'clang', 'clank', 'clans', 'claps', 'clash', 'clasp', 'class', 'clave', 'claws', 'clays', 'clean', 'clear', 'cleat', 'clefs', 'cleft', 'clerk', 'clews', 'click', 'cliff', 
'climb', 'clime', 'cline', 'cling', 'clink', 'clips', 'cloak', 'clock', 'clods', 'clogs', 'clomp', 'clone', 'close', 'cloth', 'clots', 'cloud', 'clout', 'clove', 'clown', 'cloys', 
'clubs', 'cluck', 'clued', 'clues', 'clump', 'clung', 'clunk', 'coach', 'coals', 'coast', 'coati', 'cobia', 'cobra', 'cocas', 'cocci', 'cocks', 'cocky', 'cocoa', 'cocos', 'codas', 
'codec', 'coded', 'coder', 'codes', 'codex', 'codon', 'coeds', 'cohos', 'coifs', 'coils', 'coked', 'cokes', 'colas', 'colds', 'coles', 'colic', 'colin', 'colon', 'color', 'colts', 
'comas', 'combo', 'combs', 'comer', 'comes', 'comet', 'comfy', 'comic', 'comma', 'compo', 'comps', 'comte', 'conch', 'condo', 'coned', 'cones', 'coney', 'conga', 'congo', 'conic', 
'conks', 'cooch', 'cooed', 'cooks', 'cooky', 'cools', 'coons', 'coops', 'coots', 'coped', 'coper', 'copes', 'copra', 'copse', 'coqui', 'coral', 'cords', 'cordy', 'cored', 'corer', 
'cores', 'corgi', 'corks', 'corky', 'corms', 'corns', 'cornu', 'corny', 'corps', 'coset', 'costa', 'costs', 'cotes', 'cotta', 'couch', 'cough', 'could', 'count', 'coupe', 'coups', 
'court', 'couth', 'coven', 'cover', 'coves', 'covet', 'covey', 'cower', 'cowls', 'cowry', 'coxed', 'coxes', 'coyer', 'coyly', 'coypu', 'cozen', 'crabs', 'crack', 'craft', 'crags', 
'cramp', 'crams', 'crane', 'crank', 'crape', 'craps', 'crash', 'crass', 'crate', 'crave', 'crawl', 'craws', 'craze', 'crazy', 'creak', 'cream', 'credo', 'creed', 'creek', 'creel', 
'creep', 'creme', 'crepe', 'crept', 'cress', 'crest', 'cribs', 'crick', 'cried', 'crier', 'cries', 'crime', 'crimp', 'crink', 'crisp', 'crits', 'croak', 'crock', 'crocs', 'croft', 
'crone', 'crony', 'crook', 'croon', 'crops', 'cross', 'croup', 'crowd', 'crown', 'crows', 'crude', 'cruds', 'cruel', 'cruet', 'cruft', 'crumb', 'crump', 'cruse', 'crush', 'crust', 
'crypt', 'cubby', 'cubed', 'cuber', 'cubes', 'cubic', 'cubit', 'cuddy', 'cuffs', 'cuing', 'cukes', 'culls', 'culpa', 'cults', 'cumin', 'cunts', 'cupid', 'cuppa', 'cuppy', 'curbs', 
'curds', 'curdy', 'cured', 'curer', 'cures', 'curie', 'curio', 'curls', 'curly', 'curry', 'curse', 'curve', 'curvy', 'cushy', 'cusps', 'cuspy', 'cuter', 'cutie', 'cutis', 'cutup', 
'cyber', 'cycad', 'cycle', 'cyclo', 'cynic', 'czars', 'dacha', 'daddy', 'dados', 'daffy', 'daily', 'dairy', 'daisy', 'dales', 'dally', 'dames', 'damns', 'damps', 'dance', 'dandy', 
'dared', 'darer', 'dares', 'darks', 'darns', 'darts', 'dashi', 'dashy', 'dated', 'dater', 'dates', 'datum', 'daubs', 'daunt', 'davit', 'dawns', 'dazed', 'dazes', 'deads', 'deals', 
'dealt', 'deans', 'dears', 'death', 'debar', 'debit', 'debts', 'debug', 'debut', 'decaf', 'decal', 'decay', 'decks', 'decor', 'decoy', 'decry', 'deeds', 'deems', 'deeps', 'deers', 
'defer', 'defog', 'degas', 'degum', 'deice', 'deify', 'deign', 'deism', 'deist', 'deity', 'dekes', 'delay', 'delft', 'delis', 'dells', 'delta', 'delve', 'demit', 'demon', 'demos', 
'demur', 'denim', 'dense', 'dents', 'depot', 'depth', 'deque', 'derby', 'desex', 'desks', 'deter', 'detox', 'deuce', 'devil', 'dewar', 'dewed', 'dewey', 'dhikr', 'dhows', 'dials', 
'diary', 'diced', 'dicer', 'dices', 'dicey', 'dicks', 'dicky', 'dicot', 'dicta', 'dictu', 'dicut', 'diddy', 'didos', 'didot', 'didst', 'diems', 'diest', 'dieth', 'diets', 'digit', 
'dikes', 'dildo', 'dills', 'dilly', 'dimer', 'dimes', 'dimly', 'dinar', 'dined', 'diner', 'dines', 'dingo', 'dings', 'dingy', 'dinks', 'dinky', 'dinos', 'dints', 'diode', 'dipso', 
'direr', 'dirge', 'dirks', 'dirts', 'dirty', 'disco', 'discs', 'dishy', 'disks', 'ditch', 'ditsy', 'ditto', 'ditty', 'ditzy', 'divan', 'divas', 'dived', 'diver', 'divot', 'divvy', 
'dixit', 'dizzy', 'djinn', 'docks', 'dodge', 'dodgy', 'dodos', 'doers', 'doest', 'doeth', 'doffs', 'doges', 'doggo', 'doggy', 'dogie', 'dogma', 'doily', 'doing', 'dolce', 'doled', 
'doles', 'dolls', 'dolly', 'dolor', 'dolts', 'domed', 'domes', 'donee', 'dongs', 'donna', 'donor', 'donut', 'dooms', 'doomy', 'doors', 'doozy', 'doped', 'dopes', 'dopey', 
'dorks', 'dorky', 'dorms', 'dosas', 'dosed', 'doser', 'doses', 'doted', 'doter', 'dotes', 'dotty', 'doubt', 'dough', 'doula', 'douse', 'doves', 'dovey', 'dowdy', 'dowel', 'dower', 
'downs', 'downy', 'dowry', 'dowse', 'doxie', 'doyen', 'dozed', 'dozen', 'dozer', 'dozes', 'drabs', 'draft', 'drags', 'drain', 'drake', 'drama', 'drams', 'drank', 'drape', 'drawl', 
'drawn', 'draws', 'drays', 'dread', 'dream', 'drear', 'dreck', 'dregs', 'dress', 'dribs', 'dried', 'drier', 'dries', 'drift', 'drill', 'drily', 'drink', 'drive', 'droid', 'droit', 
'droll', 'drone', 'drool', 'droop', 'drops', 'dross', 'drove', 'drown', 'drubs', 'drugs', 'druid', 'drums', 'drunk', 'drupe', 'dryad', 'dryer', 'dryly', 'ducal', 'ducat', 'duces', 
'duchy', 'ducks', 'ducky', 'ducts', 'duddy', 'dudes', 'duels', 'duets', 'duffs', 'dukes', 'dulls', 'dully', 'dulse', 'dumbo', 'dummy', 'dumps', 'dumpy', 'dunce', 'dunes', 'dungs', 
'dungy', 'dunks', 'dunno', 'duomo', 'duped', 'duper', 'dupes', 'duple', 'dural', 'durst', 'durum', 'dusks', 'dusky', 'dusts', 'dusty', 'dutch', 'duvet', 'dwarf', 'dweeb', 'dwell', 
'dwelt', 'dyads', 'dyers', 'dying', 'dykes', 'dynes', 'eager', 'eagle', 'eared', 'earls', 'early', 'earns', 'earth', 'eased', 'easel', 'easer', 'easts', 'eaten', 'eater', 'eaves', 
'ebbed', 'ebony', 'ebook', 'echos', 'eclat', 'edema', 'edged', 'edger', 'edges', 'edict', 'edify', 'edits', 'educe', 'eejit', 'eerie', 'egged', 'egger', 'egret', 'eider', 'eidos', 
'eight', 'eject', 'ejido', 'eking', 'eland', 'elans', 'elate', 'elbow', 'elder', 'elect', 'elegy', 'elfin', 'elide', 'elite', 'elope', 'elude', 'elute', 'elven', 'elves', 'email', 
'embed', 'ember', 'emcee', 'emend', 'emery', 'emirs', 'emits', 'emote', 'empty', 'enact', 'ended', 'ender', 'endow', 'endue', 'enema', 'enemy', 'enjoy', 'ennui', 'enoki', 'enrol', 
'ensue', 'enter', 'entry', 'envoi', 'envoy', 'eosin', 'epact', 'epees', 'ephah', 'ephod', 'epics', 'epoch', 'epoxy', 'epsom', 'equal', 'equip', 'erase', 'erect', 'ergot', 'erode', 
'erred', 'error', 'eruct', 'erupt', 'essay', 'esses', 'ester', 'estop', 'etext', 'ether', 'ethic', 'ethos', 'ethyl', 'etude', 'evade', 'evens', 'event', 'every', 'evict', 'evils', 
'evoke', 'ewers', 'exact', 'exalt', 'exams', 'excel', 'excon', 'exeat', 'execs', 'exert', 'exile', 'exist', 'exits', 'expel', 'expos', 'extol', 'extra', 'exude', 'exult', 'exurb', 
'eyers', 'eying', 'eyrie', 'fable', 'faced', 'facer', 'faces', 'facet', 'facia', 'facie', 'facto', 'facts', 'faded', 'fader', 'fades', 'faery', 'fagot', 'fails', 'faint', 'faire', 
'fairs', 'fairy', 'faith', 'faked', 'faker', 'fakes', 'fakie', 'fakir', 'falls', 'false', 'famed', 'fancy', 'fangs', 'fanin', 'fanny', 'farad', 'farce', 'fared', 'fares', 'farms', 
'farts', 'fasts', 'fatal', 'fated', 'fates', 'fatly', 'fatso', 'fatty', 'fatwa', 'fault', 'fauna', 'fauns', 'favas', 'faves', 'favor', 'fawns', 'fawny', 'faxed', 'faxer', 'faxes', 
'fazed', 'fazes', 'fears', 'feast', 'feats', 'fecal', 'feces', 'feeds', 'feels', 'feign', 'feist', 'fella', 'fells', 'felon', 'felts', 'femme', 'femur', 'fence', 'fends', 'fenny', 
'feral', 'feria', 'fermi', 'ferns', 'ferny', 'ferry', 'fests', 'fetal', 'fetch', 'fetes', 'fetid', 'fetor', 'fetus', 'feuar', 'feuds', 'feued', 'fever', 'fewer', 'fiats', 'fiber', 
'fibre', 'fiche', 'fichu', 'ficus', 'fiefs', 'field', 'fiend', 'fiery', 'fifth', 'fifty', 'fight', 'filar', 'filch', 'filed', 'filer', 'files', 'filet', 'fills', 'filly', 'films', 
'filmy', 'filth', 'final', 'finca', 'finch', 'finds', 'fined', 'finer', 'fines', 'finif', 'finis', 'finks', 'finny', 'fiord', 'fired', 'firer', 'fires', 'firma', 'firms', 'first', 
'firth', 'fishy', 'fists', 'fisty', 'fitly', 'fiver', 'fives', 'fixer', 'fixes', 'fixit', 'fizzy', 'fjord', 'flabs', 'flack', 'flags', 'flail', 'flair', 'flake', 'flaks', 'flaky', 
'flame', 'flams', 'flank', 'flans', 'flaps', 'flare', 'flash', 'flask', 'flats', 'flaws', 'flays', 'fleas', 'fleck', 'flees', 'fleet', 'flesh', 'flick', 'flics', 'flied', 'flier', 
'flies', 'fling', 'flint', 'flips', 'flirt', 'flits', 'float', 'flock', 'floes', 'flogs', 'flood', 'floor', 'flops', 'flora', 'floss', 'flour', 'flout', 'flown', 'flows', 'flubs', 
'flues', 'fluff', 'fluid', 'fluke', 'fluky', 'flume', 'flung', 'flunk', 'flush', 'flute', 'flyby', 'flyer', 'foals', 'foams', 'foamy', 'focal', 'focus', 'fogey', 'foggy', 'foils', 
'foist', 'folds', 'folia', 'folic', 'folio', 'folks', 'folly', 'fondu', 'fonts', 'foods', 'fools', 'foots', 'foray', 'force', 'fords', 'fores', 'forge', 'forgo', 'forks', 'forky', 
'forma', 'forms', 'forte', 'forth', 'forts', 'forty', 'forum', 'fossa', 'fosse', 'fouls', 'found', 'fount', 'fours', 'fovea', 'fowls', 'foxed', 'foxes', 'foyer', 'frail', 'frame', 
'franc', 'frank', 'frats', 'fraud', 'frays', 'freak', 'freed', 'freer', 'frees', 'fresh', 'frets', 'friar', 'fried', 'frier', 'fries', 'frigs', 'frill', 'frisk', 'fritz', 'frizz', 
'frock', 'frogs', 'frond', 'front', 'frosh', 'frost', 'froth', 'frown', 'froze', 'fruit', 'frump', 'fryer', 'ftped', 'fucks', 'fudge', 'fudgy', 'fuels', 'fugal', 'fugit', 'fugue', 
'fulls', 'fully', 'fumed', 'fumer', 'fumes', 'funds', 'fungi', 'fungo', 'funks', 'funky', 'funny', 'furls', 'furor', 'furry', 'furze', 'fused', 'fusee', 'fuses', 'fussy', 'fusty', 
'futon', 'fuzed', 'fuzes', 'fuzzy', 'gabby', 'gable', 'gaffe', 'gaffs', 'gages', 'gaily', 'gains', 'gaits', 'galas', 'gales', 'galls', 'gamba', 'gamed', 'gamer', 'games', 'gamey', 
'gamic', 'gamin', 'gamma', 'gamut', 'ganef', 'gangs', 'gaped', 'gaper', 'gapes', 'gappy', 'garbs', 'garde', 'gases', 'gasps', 'gassy', 'gated', 'gates', 'gator', 'gaudy', 'gauge', 
'gaunt', 'gauss', 'gauze', 'gauzy', 'gavel', 'gawky', 'gayer', 'gayly', 'gazed', 'gazer', 'gazes', 'gears', 'gecko', 'geeks', 'geeky', 'geese', 'gelds', 'genes', 'genet', 'genie', 
'genii', 'genre', 'gents', 'genus', 'geode', 'germs', 'gesso', 'getup', 'ghost', 'ghoti', 'ghoul', 'giant', 'gibed', 'giber', 'gibes', 'giddy', 'gifts', 'gigas', 'gigue', 'gilds', 
'gills', 'gilts', 'gimel', 'gimme', 'gimpy', 'ginny', 'gipsy', 'girds', 'girls', 'girly', 'giros', 'girth', 'girts', 'gismo', 'gists', 'given', 'giver', 'gives', 'gizmo', 'glade', 
'glads', 'gland', 'glans', 'glare', 'glary', 'glass', 'glaze', 'gleam', 'glean', 'glebe', 'glees', 'glens', 'glide', 'glint', 'glitz', 'gloat', 'globe', 'globs', 'gloms', 'gloom', 
'glory', 'gloss', 'glove', 'glued', 'gluer', 'glues', 'gluey', 'gluon', 'gluts', 'glyph', 'gnarl', 'gnash', 'gnats', 'gnaws', 'gnome', 'goads', 'goals', 'goats', 'godly', 'goers', 
'goest', 'goeth', 'going', 'golds', 'golem', 'golfs', 'golly', 'gonad', 'goner', 'gongs', 'gonna', 'gonzo', 'goods', 'goody', 'gooey', 'goofs', 'goofy', 'gooks', 'gooky', 'goons', 
'goony', 'goose', 'goosy', 'gored', 'gores', 'gorge', 'gorse', 'goths', 'gotta', 'gouda', 'gouge', 'gourd', 'gouts', 'gouty', 'gowns', 'goyim', 'grabs', 'grace', 'grade', 'grads', 
'graft', 'grail', 'grain', 'grams', 'grand', 'grant', 'grape', 'graph', 'grapy', 'grasp', 'grass', 'grata', 'grate', 'grave', 'gravy', 'grays', 'graze', 'great', 'grebe', 'greed', 
'green', 'greet', 'greps', 'greys', 'grids', 'grief', 'grift', 'grill', 'grime', 'grimy', 'grind', 'grins', 'gripe', 'grips', 'grist', 'grits', 'groan', 'groat', 'grody', 'groin', 
'groks', 'gronk', 'grook', 'groom', 'grope', 'gross', 'group', 'grout', 'grove', 'growl', 'grown', 'grows', 'grubs', 'gruel', 'gruff', 'grump', 'grunt', 'guano', 'guard', 'guava', 
'guess', 'guest', 'guide', 'guild', 'guile', 'guilt', 'guise', 'gulag', 'gulch', 'gules', 'gulfs', 'gulls', 'gully', 'gulps', 'gumbo', 'gummy', 'gunks', 'gunky', 'guppy', 'gurus', 
'gushy', 'gusto', 'gusts', 'gusty', 'gutsy', 'gutta', 'gutty', 'guyed', 'gwine', 'gyppy', 'gypsy', 'gyros', 'gyved', 'gyves', 'habit', 'hacks', 'hadda', 'hadst', 'hafta', 'hafts', 
'haiku', 'hails', 'hairs', 'hairy', 'haled', 'haler', 'hales', 'hallo', 'halls', 'halma', 'halos', 'halts', 'halve', 'hames', 'hammy', 'hamza', 'handy', 'hangs', 'hanks', 'hanky', 
'hapax', 'haply', 'happy', 'hardy', 'harem', 'hares', 'harks', 'harms', 'harps', 'harpy', 'harry', 'harsh', 'harts', 'harum', 'hasps', 'haste', 'hasty', 'hatch', 'hated', 'hater', 
'hates', 'hauls', 'haunt', 'haute', 'haven', 'haves', 'havoc', 'hawed', 'hawks', 'hayed', 'hayer', 'hayey', 'hazed', 'hazel', 'hazer', 'heads', 'heady', 'heals', 'heaps', 'heard', 
'hears', 'heart', 'heath', 'heats', 'heave', 'heavy', 'hedge', 'heeds', 'heels', 'heerd', 'hefts', 'hefty', 'heigh', 'heirs', 'heist', 'helix', 'hello', 'hells', 'helms', 'helps', 
'hemps', 'hempy', 'hence', 'henge', 'henna', 'henry', 'herbs', 'herby', 'herds', 'herem', 'heres', 'heron', 'heros', 'hertz', 'hewer', 'hexad', 'hexed', 'hexer', 'hexes', 'hicks', 
'hider', 'hides', 'highs', 'hiked', 'hiker', 'hikes', 'hilar', 'hills', 'hilly', 'hilts', 'hilum', 'himbo', 'hinds', 'hinge', 'hints', 'hippo', 'hippy', 'hired', 'hirer', 'hires', 
'hitch', 'hived', 'hiver', 'hives', 'hoagy', 'hoard', 'hoars', 'hoary', 'hobby', 'hobos', 'hocks', 'hocus', 'hodad', 'hogan', 'hoist', 'hokey', 'hokum', 'holds', 'holed', 'holer', 
'holes', 'holey', 'holly', 'holon', 'homed', 'homer', 'homes', 'homey', 'homme', 'homos', 'honed', 'honer', 'honey', 'honks', 'honky', 'honor', 'hooch', 'hoods', 'hooey', 'hoofs', 
'hooks', 'hooky', 'hoops', 'hoots', 'hoped', 'hoper', 'hopes', 'hoppy', 'horde', 'horns', 'horny', 'horse', 'horsy', 'hosed', 'hoses', 'hosts', 'hotel', 'hotly', 'hound', 'houri', 
'hours', 'house', 'hovel', 'hover', 'howdy', 'howls', 'hubba', 'hubby', 'huffs', 'huffy', 'huger', 'hulks', 'hulky', 'hullo', 'hulls', 'human', 'humid', 'humor', 'humpf', 'humph', 
'humps', 'humpy', 'humus', 'hunch', 'hunks', 'hunky', 'hunts', 'hurls', 'hurly', 'hurry', 'husks', 'husky', 'hussy', 'hutch', 'huzza', 'hydra', 'hydro', 'hyena', 'hying', 'hymen', 
'hymns', 'hyped', 'hyper', 'hypes', 'hypos', 'iambs', 'icers', 'ichor', 'icier', 'icily', 'icing', 'icons', 'ideal', 'ideas', 'idiom', 'idiot', 'idled', 'idler', 'idles', 'idols', 
'idyll', 'idyls', 'igloo', 'ikats', 'ikons', 'ileum', 'ileus', 'iliac', 'ilium', 'image', 'imago', 'imams', 'imbed', 'imbue', 'immix', 'impel', 'imply', 'impro', 'inane', 'inapt', 
'inbox', 'incur', 'index', 'indie', 'inept', 'inert', 'infer', 'infix', 'infra', 'ingot', 'injun', 'inked', 'inker', 'inlay', 'inlet', 'inner', 'inode', 'input', 'inset', 'inter', 
'intra', 'intro', 'inure', 'iodic', 'ionic', 'iotas', 'irate', 'irked', 'irony', 'isles', 'islet', 'issue', 'itchy', 'items', 'ivied', 'ivies', 'ivory', 'ixnay', 'jacks', 
'jaded', 'jades', 'jaggy', 'jails', 'jakes', 'jambs', 'jammy', 'janes', 'jaunt', 'jawed', 'jazzy', 'jeans', 'jeeps', 'jeers', 'jello', 'jells', 'jelly', 'jenny', 'jerks', 'jerky', 
'jerry', 'jests', 'jetty', 'jewel', 'jibed', 'jiber', 'jibes', 'jiffy', 'jihad', 'jilts', 'jimmy', 'jingo', 'jings', 'jinks', 'jinns', 'jived', 'jives', 'jocks', 'joeys', 'johns', 
'joins', 'joint', 'joist', 'joked', 'joker', 'jokes', 'jolly', 'jolts', 'joule', 'joust', 'jowls', 'jowly', 'joyed', 'judge', 'judos', 'juice', 'juicy', 'jujus', 'jukes', 'julep', 
'jumbo', 'jumps', 'jumpy', 'junco', 'junks', 'junky', 'junta', 'junto', 'juror', 'juste', 'jutes', 'kabob', 'kaiak', 'kales', 'kapok', 'kappa', 'kaput', 'karat', 'karma', 'kayak', 
'kayos', 'kazoo', 'kebab', 'kebob', 'keels', 'keens', 'keeps', 'kelly', 'kelps', 'kelpy', 'kenaf', 'kepis', 'kerbs', 'kerfs', 'kerns', 'ketch', 'keyed', 'keyer', 'khaki', 'khans', 
'kicks', 'kicky', 'kiddo', 'kikes', 'kills', 'kilns', 'kilts', 'kilty', 'kinda', 'kinds', 'kings', 'kinks', 'kinky', 'kiosk', 'kirks', 'kited', 'kites', 'kiths', 'kitty', 'kivas', 
'kiwis', 'klieg', 'kluge', 'klugy', 'klunk', 'knack', 'knave', 'knead', 'kneed', 'kneel', 'knees', 'knell', 'knelt', 'knife', 'knish', 'knits', 'knobs', 'knock', 'knoll', 'knops', 
'knots', 'knout', 'known', 'knows', 'koala', 'koine', 'kooks', 'kooky', 'kopek', 'kraal', 'kraut', 'krill', 'krona', 'krone', 'kudos', 'kudzu', 'kulak', 'kyrie', 'label', 'labia', 
'labor', 'laced', 'lacer', 'lacey', 'lacks', 'laded', 'laden', 'lades', 'ladle', 'lager', 'laird', 'lairs', 'laity', 'laker', 'lakes', 'lamas', 'lambs', 'lamed', 'lamer', 'lames', 
'lamps', 'lanai', 'lance', 'lands', 'lanes', 'lanky', 'lapel', 'lapin', 'lapis', 'lapse', 'larch', 'lards', 'lardy', 'large', 'largo', 'larks', 'larva', 'lased', 'laser', 'lases', 
'lasso', 'lasts', 'latch', 'later', 'latex', 'lathe', 'laths', 'latte', 'latus', 'laude', 'lauds', 'laugh', 'lavas', 'laved', 'laver', 'laves', 'lawns', 'lawny', 'lawzy', 
'laxer', 'laxly', 'layer', 'lazed', 'lazes', 'leach', 'leads', 'leafs', 'leafy', 'leaks', 'leaky', 'leans', 'leant', 'leaps', 'leapt', 'learn', 'lease', 'leash', 'least', 'leave', 
'ledge', 'leech', 'leers', 'leery', 'lefts', 'lefty', 'legal', 'leggo', 'leggy', 'legit', 'legos', 'lemma', 'lemme', 'lemon', 'lemur', 'lends', 'lento', 'leper', 'lepta', 'letup', 
'levee', 'level', 'lever', 'levis', 'liars', 'libel', 'libra', 'licit', 'licks', 'liege', 'liens', 'liers', 'liest', 'lieth', 'lifer', 'lifts', 'light', 'ligne', 'liked', 'liken', 
'liker', 'lilac', 'lilts', 'lilty', 'limbo', 'limbs', 'limby', 'limed', 'limen', 'limes', 'limey', 'limit', 'limns', 'limos', 'limps', 'lined', 'linen', 'liner', 'lines', 'lingo', 
'links', 'lints', 'linty', 'lions', 'lipid', 'lippy', 'liras', 'lisle', 'lisps', 'lists', 'liter', 'lites', 'lithe', 'litho', 'litre', 'lived', 'liven', 'liver', 'lives', 'livid', 
'livre', 'llama', 'loads', 'loafs', 'loams', 'loamy', 'loans', 'loath', 'lobar', 'lobby', 'lobed', 'lobes', 'local', 'lochs', 'locks', 'locos', 'locus', 'lodes', 'lodge', 'lofts', 
'lofty', 'loges', 'loggy', 'logic', 'login', 'logos', 'loins', 'lolls', 'lolly', 'loner', 'longs', 'looks', 'looky', 'looms', 'loons', 'loony', 'loops', 'loopy', 'loose', 'loots', 
'loped', 'loper', 'lopes', 'loppy', 'lords', 'lordy', 'lores', 'lorry', 'loser', 'loses', 'lossy', 'lotsa', 'lotta', 'lotto', 'lotus', 'louis', 'louse', 'lousy', 'loved', 'lover', 
'loves', 'lowed', 'lower', 'lowly', 'loxes', 'loyal', 'luaus', 'lubes', 'lubra', 'lucid', 'lucks', 'lucky', 'lucre', 'lulab', 'lulls', 'lulus', 'lumen', 'lumpy', 'lunar', 'lunch', 
'lunes', 'lunge', 'lungs', 'lupus', 'lurch', 'lured', 'lurer', 'lures', 'lurid', 'lurks', 'lusts', 'lusty', 'luted', 'lutes', 'luvya', 'luxes', 'lying', 'lymph', 'lynch', 'lyres', 
'lyric', 'macaw', 'maced', 'macer', 'maces', 'macho', 'macro', 'madam', 'madly', 'mafia', 'magic', 'magma', 'magna', 'magus', 'mahua', 'mails', 'maims', 'mains', 'maize', 'major', 
'maker', 'makes', 'males', 'malls', 'malts', 'malty', 'mamas', 'mambo', 'mamma', 'mammy', 'maned', 'manes', 'manga', 'mange', 'mango', 'mangy', 'mania', 'manic', 'manly', 'manna', 
'manor', 'manse', 'manta', 'maple', 'march', 'mares', 'marge', 'maria', 'marks', 'marls', 'marry', 'marsh', 'marts', 'maser', 'mashy', 'mason', 'masse', 'masts', 'match', 'mated', 
'mater', 'mates', 'matey', 'maths', 'matte', 'matzo', 'mauls', 'mauve', 'maven', 'mavis', 'maxim', 'maxis', 'maybe', 'mayor', 'mazed', 'mazer', 'mazes', 'meads', 'meals', 'mealy', 
'means', 'meant', 'meany', 'meats', 'meaty', 'mebbe', 'mecca', 'mecum', 'medal', 'media', 'medic', 'meets', 'melba', 'melee', 'melon', 'melts', 'memes', 'memos', 'mends', 'menus', 
'meows', 'mercy', 'merge', 'merit', 'merry', 'merse', 'mesas', 'mesne', 'meson', 'messy', 'metal', 'meted', 'meter', 'metes', 'metre', 'metro', 'mewed', 'mezzo', 'miaow', 'micas', 
'micks', 'micro', 'middy', 'midge', 'midis', 'midst', 'miens', 'miffs', 'might', 'miked', 'mikes', 'milch', 'miler', 'milks', 'milky', 'mills', 'mimed', 'mimeo', 'mimer', 'mimes', 
'mimic', 'mimsy', 'minas', 'mince', 'minds', 'mined', 'miner', 'mines', 'minim', 'minis', 'minks', 'minor', 'minty', 'minus', 'mired', 'mires', 'mirth', 'miser', 'missy', 'mists', 
'misty', 'miter', 'mites', 'mitre', 'mitts', 'mixed', 'mixer', 'mixes', 'mixup', 'moans', 'moats', 'mocha', 'modal', 'model', 'modem', 'modes', 'modus', 'mogul', 'mohel', 'moire', 
'moist', 'molal', 'molar', 'molas', 'molds', 'moldy', 'moles', 'molls', 'molly', 'molto', 'molts', 'mommy', 'monad', 'mondo', 'money', 'monic', 'monks', 'monte', 'month', 'mooch', 
'moods', 'moody', 'mooed', 'moola', 'moons', 'moony', 'moors', 'moose', 'moots', 'moped', 'mopes', 'moral', 'moray', 'morel', 'mores', 'morns', 'moron', 'morph', 'morts', 'mosey', 
'mossy', 'mosts', 'motel', 'motes', 'motet', 'moths', 'mothy', 'motif', 'motor', 'motto', 'mould', 'moult', 'mound', 'mount', 'mourn', 'mouse', 'mousy', 'mouth', 'moved', 'mover', 
'moves', 'movie', 'mowed', 'mower', 'moxie', 'mrads', 'mucho', 'mucks', 'mucky', 'mucus', 'muddy', 'muffs', 'mufti', 'muggy', 'mujik', 'mulch', 'mulct', 'mules', 'muley', 'mulls', 
'mumbo', 'mummy', 'mumps', 'munch', 'munge', 'mungs', 'mungy', 'muons', 'mural', 'murky', 'mused', 'muser', 'muses', 'mushy', 'music', 'musks', 'musky', 'musos', 'mussy', 'musta', 
'musts', 'musty', 'muted', 'muter', 'mutes', 'mutts', 'muxes', 'mylar', 'mynas', 'myrrh', 'myths', 'nabla', 'nabob', 'nacho', 'nadir', 'naiad', 'nails', 'naive', 'naked', 'named', 
'namer', 'names', 'nanny', 'napes', 'nappy', 'narco', 'narcs', 'nares', 'nasal', 'nasty', 'natal', 'natch', 'nates', 'natty', 'naval', 'navel', 'naves', 'nears', 'neath', 'neato', 
'necks', 'needs', 'needy', 'negro', 'neigh', 'neons', 'nerdy', 'nerfs', 'nerts', 'nerve', 'nervy', 'nests', 'never', 'newel', 'newer', 'newly', 'newsy', 'newts', 'nexus', 'nicad', 
'nicer', 'niche', 'nicks', 'niece', 'nifty', 'night', 'nihil', 'nimbi', 'nines', 'ninja', 'ninny', 'ninth', 'nippy', 'nisei', 'niter', 'nitro', 'nitty', 'nixed', 'nixes', 'nixie', 
'nobby', 'noble', 'nobly', 'nodal', 'noddy', 'noels', 'nohow', 'noire', 'noise', 'noisy', 'nomad', 'nonce', 'nones', 'nonny', 'nooks', 'nooky', 'noons', 'noose', 'norms', 'north', 
'nosed', 'noses', 'nosey', 'notch', 'noter', 'notes', 'nouns', 'novae', 'novas', 'novel', 'noway', 'nuder', 'nudes', 'nudge', 'nudie', 'nuked', 'nukes', 'nulls', 'numbs', 'nurbs', 
'nurse', 'nutsy', 'nutty', 'nylon', 'nymph', 'oaken', 'oakum', 'oared', 'oases', 'oasis', 'oaten', 'oaths', 'obeah', 'obese', 'obeys', 'obits', 'oboes', 'occur', 'ocean', 'ocher', 
'ochre', 'octal', 'octet', 'odder', 'oddly', 'odium', 'odors', 'odour', 'offal', 'offed', 'offen', 'offer', 'often', 'ogled', 'ogler', 'ogles', 'ogres', 'ohhhh', 'ohmic', 'oiled', 
'oiler', 'oinks', 'oinky', 'okays', 'okras', 'olden', 'older', 'oldie', 'oleos', 'olios', 'olive', 'ombre', 'omega', 'omens', 'omits', 'oncet', 'onion', 'onset', 'oodle', 'oomph', 
'oozed', 'oozes', 'opens', 'opera', 'opine', 'opium', 'opted', 'optic', 'orals', 'orate', 'orbed', 'orbit', 'orcas', 'order', 'organ', 'oring', 'orlon', 'ortho', 'osier', 'other', 
'otter', 'ought', 'ouija', 'ounce', 'ousel', 'ousts', 'outdo', 'outen', 'outer', 'outgo', 'outta', 'ouzel', 'ovals', 'ovary', 'ovate', 'ovens', 'overs', 'overt', 'ovine', 'ovoid', 
'ovule', 'owest', 'owing', 'owlet', 'owned', 'owner', 'oxbow', 'oxeye', 'oxide', 'oxlip', 'ozone', 'paced', 'pacer', 'paces', 'packs', 'pacts', 'paddy', 'padre', 'paean', 'pagan', 
'paged', 'pages', 'pails', 'pains', 'paint', 'pairs', 'paled', 'paler', 'pales', 'palls', 'pally', 'palms', 'palmy', 'palsy', 'pampa', 'panda', 'paned', 'panel', 'panes', 'panga', 
'panic', 'pansy', 'pants', 'panty', 'papal', 'papas', 'papaw', 'paper', 'pappy', 'paras', 'parch', 'pards', 'pared', 'paren', 'parer', 'pares', 'parka', 'parks', 'parry', 'parse', 
'parts', 'party', 'pasha', 'passe', 'pasta', 'paste', 'pasts', 'pasty', 'patch', 'paten', 'pater', 'pates', 'paths', 'patio', 'patsy', 'patty', 'pause', 'pavan', 'paved', 'paves', 
'pawed', 'pawer', 'pawky', 'pawls', 'pawns', 'payed', 'payee', 'payer', 'peace', 'peach', 'peaks', 'peaky', 'peals', 'pearl', 'pears', 'pease', 'peats', 'peaty', 'pecan', 'pecks', 
'pedal', 'peeks', 'peels', 'peens', 'peeps', 'peers', 'peeve', 'pekoe', 'pelts', 'penal', 'pence', 'pends', 'penes', 'pengo', 'penis', 'penne', 'penny', 'peons', 'peony', 'perch', 
'perdu', 'peril', 'perks', 'perky', 'perms', 'pesky', 'pesos', 'pesto', 'pests', 'petal', 'peter', 'petit', 'petri', 'petty', 'pewee', 'pewit', 'pffft', 'phage', 'phase', 'phial', 
'phlox', 'phone', 'phony', 'photo', 'phyla', 'piano', 'picas', 'picks', 'picky', 'picot', 'piece', 'piers', 'pieta', 'piety', 'piggy', 'pigmy', 'piing', 'piker', 'pilaf', 'pilau', 
'piled', 'piles', 'pills', 'pilot', 'pimps', 'pinch', 'pined', 'pines', 'piney', 'pings', 'pinko', 'pinks', 'pinky', 'pinto', 'pints', 'pinup', 'pions', 'piped', 'piper', 'pipes', 
'pipet', 'pique', 'pismo', 'pitas', 'pitch', 'piths', 'pithy', 'piton', 'pivot', 'pixel', 'pixie', 'pizza', 'place', 'plaid', 'plain', 'plait', 'plane', 'plank', 'plans', 'plant', 
'plash', 'plasm', 'plate', 'plats', 'playa', 'plays', 'plaza', 'plead', 'pleas', 'pleat', 'plebe', 'plebs', 'plein', 'plena', 'plied', 'plier', 'plies', 'plods', 'plonk', 'plops', 
'plots', 'plows', 'ploys', 'pluck', 'plugs', 'plumb', 'plume', 'plump', 'plums', 'plumy', 'plunk', 'plush', 'plyer', 'poach', 'pocks', 'pocky', 'podia', 'poems', 'poesy', 'poets', 
'point', 'poise', 'poked', 'poker', 'pokes', 'pokey', 'polar', 'poled', 'poler', 'poles', 'polio', 'polis', 'polka', 'polls', 'polly', 'polyp', 'pomps', 'ponds', 'pones', 'pooch', 
'pooey', 'poohs', 'pools', 'poops', 'popes', 'poppy', 'porch', 'pored', 'pores', 'porgy', 'porks', 'porky', 'porno', 'ports', 'poser', 'poses', 'poset', 'posit', 'posse', 'poste', 
'posts', 'potty', 'pouch', 'poufs', 'pound', 'pours', 'pouts', 'pouty', 'power', 'poxed', 'poxes', 'prams', 'prank', 'prate', 'prawn', 'prays', 'preen', 'preps', 'press', 'prest', 
'prexy', 'preys', 'price', 'prick', 'pride', 'pried', 'prier', 'pries', 'prigs', 'prima', 'prime', 'primo', 'primp', 'prink', 'print', 'prior', 'prise', 'prism', 'privy', 'prize', 
'probe', 'prods', 'proem', 'profs', 'promo', 'proms', 'prone', 'prong', 'proof', 'props', 'prose', 'prosy', 'proud', 'prove', 'prowl', 'prows', 'proxy', 'prude', 'prune', 'pruta', 
'pryer', 'psalm', 'pseud', 'pshaw', 'psoas', 'pssst', 'psych', 'pubes', 'pubic', 'pubis', 'pucks', 'pudgy', 'puffy', 'puked', 'pukes', 'pukka', 'pulls', 'pulps', 'pulpy', 'pulse', 
'pumas', 'pumps', 'punch', 'punks', 'punky', 'punny', 'punts', 'pupae', 'pupal', 'pupas', 'pupil', 'puppy', 'puree', 'purer', 'purge', 'purls', 'purrs', 'purse', 'purty', 'pushy', 
'pussy', 'putts', 'putty', 'pygmy', 'pylon', 'pyres', 'pyxie', 'qophs', 'quack', 'quads', 'quaff', 'quail', 'quais', 'quake', 'qualm', 'quals', 'quark', 'quart', 'quash', 'quasi', 
'quays', 'queen', 'queer', 'quell', 'query', 'quest', 'queue', 'quick', 'quids', 'quiet', 'quiff', 'quill', 'quilt', 'quint', 'quips', 'quipu', 'quire', 'quirk', 'quirt', 'quite', 
'quits', 'quoin', 'quoit', 'quota', 'quote', 'quoth', 'rabbi', 'rabid', 'raced', 'racer', 'races', 'radar', 'radii', 'radio', 'radix', 'radon', 'rafts', 'raged', 'rages', 'raids', 
'rails', 'rains', 'rainy', 'raise', 'rajah', 'rajas', 'raked', 'raker', 'rakes', 'rally', 'ralph', 'ramen', 'ranch', 'rands', 'randy', 'range', 'rangy', 'ranks', 'rants', 'raped', 
'raper', 'rapes', 'rapid', 'rarer', 'rasae', 'rasps', 'raspy', 'rated', 'rater', 'rates', 'raths', 'ratio', 'ratty', 'raved', 'ravel', 'raven', 'raver', 'raves', 'rawer', 'rawly', 
'rayed', 'rayon', 'razed', 'razer', 'razes', 'razor', 'reach', 'react', 'reads', 'ready', 'realm', 'reams', 'reaps', 'rearm', 'rears', 'rebar', 'rebel', 'rebid', 'rebox', 'rebus', 
'rebut', 'recap', 'recta', 'recto', 'recur', 'recut', 'redid', 'redip', 'redly', 'redox', 'reeds', 'reedy', 'reefs', 'reeks', 'reeky', 'reels', 'reeve', 'refer', 'refit', 'refix', 
'refly', 'refry', 'regal', 'rehab', 'reify', 'reign', 'reins', 'relax', 'relay', 'relic', 'reman', 'remap', 'remit', 'remix', 'renal', 'rends', 'renew', 'rente', 'rents', 'repay', 
'repel', 'reply', 'repro', 'reran', 'rerun', 'resaw', 'resay', 'reset', 'resin', 'rests', 'retch', 'retro', 'retry', 'reuse', 'revel', 'revet', 'revue', 'rewed', 'rheas', 
'rheum', 'rhino', 'rhumb', 'rhyme', 'rials', 'ribby', 'riced', 'ricer', 'rider', 'rides', 'ridge', 'ridgy', 'rifer', 'rifle', 'rifts', 'right', 'rigid', 'rigor', 'riled', 'riles', 
'rille', 'rills', 'rimed', 'rimer', 'rimes', 'rinds', 'rings', 'rinse', 'riots', 'ripen', 'riper', 'risen', 'riser', 'rises', 'risks', 'risky', 'rites', 'ritzy', 'rival', 'rived', 
'riven', 'river', 'rives', 'rivet', 'roach', 'roads', 'roans', 'roars', 'roast', 'robed', 'robes', 'robin', 'roble', 'robot', 'rocks', 'rocky', 'rodeo', 'roger', 'rogue', 'roids', 
'roils', 'roily', 'roles', 'rolls', 'roman', 'rondo', 'roods', 'roofs', 'rooks', 'rooky', 'rooms', 'roomy', 'roost', 'roots', 'rooty', 'roped', 'roper', 'ropes', 'roses', 'rosin', 
'rotor', 'rouge', 'rough', 'round', 'rouse', 'roust', 'route', 'routs', 'roved', 'rover', 'roves', 'rowan', 'rowdy', 'rowed', 'rower', 'royal', 'rubes', 'ruble', 'ruche', 'ruddy', 
'ruder', 'ruffs', 'rugby', 'ruing', 'ruled', 'ruler', 'rules', 'rumba', 'rumen', 'rummy', 'rumor', 'rumps', 'runes', 'rungs', 'runic', 'runny', 'runts', 'runty', 'rupee', 'rural', 
'ruses', 'rusks', 'russe', 'rusty', 'rutty', 'saber', 'sable', 'sabra', 'sabre', 'sacks', 'sadly', 'safer', 'safes', 'sagas', 'sager', 'sages', 'sahib', 'sails', 'saint', 'saith', 
'sakes', 'salad', 'sally', 'salon', 'salsa', 'salts', 'salty', 'salve', 'salvo', 'samba', 'sands', 'sandy', 'saner', 'sappy', 'saran', 'sarge', 'saris', 'sassy', 'sated', 'sates', 
'satin', 'satyr', 'sauce', 'saucy', 'sauna', 'saute', 'saved', 'saver', 'saves', 'savor', 'savoy', 'savvy', 'sawed', 'sawer', 'saxes', 'sayer', 'scabs', 'scads', 'scald', 'scale', 
'scalp', 'scaly', 'scamp', 'scams', 'scans', 'scant', 'scare', 'scarf', 'scarp', 'scars', 'scary', 'scats', 'scene', 'scent', 'schmo', 'schwa', 'scion', 'scoff', 'scold', 'scone', 
'scoop', 'scoot', 'scope', 'scops', 'score', 'scorn', 'scour', 'scout', 'scowl', 'scows', 'scram', 'scrap', 'scree', 'screw', 'scrim', 'scrip', 'scrod', 'scrub', 'scrum', 'scuba', 
'scudi', 'scudo', 'scuds', 'scull', 'scums', 'scurf', 'scuse', 'scuzz', 'seals', 'seams', 'seamy', 'sears', 'seats', 'sebum', 'secco', 'sects', 'sedan', 'seder', 'sedge', 'sedgy', 
'sedum', 'seeds', 'seedy', 'seeks', 'seems', 'seeps', 'seers', 'seest', 'seeth', 'segue', 'seine', 'seize', 'selah', 'selfs', 'sells', 'semen', 'semis', 'sends', 'sense', 'sepal', 
'sepia', 'sepoy', 'serfs', 'serge', 'serif', 'serum', 'serve', 'servo', 'setup', 'seven', 'sever', 'sewed', 'sewer', 'sexed', 'sexes', 'shack', 'shade', 'shads', 'shady', 'shaft', 
'shags', 'shake', 'shako', 'shaky', 'shale', 'shall', 'shalt', 'shame', 'shams', 'shank', 'shape', 'shard', 'share', 'shark', 'sharp', 'shave', 'shawl', 'shawm', 'shays', 'sheaf', 
'shear', 'sheds', 'sheen', 'sheep', 'sheer', 'sheet', 'sheik', 'shelf', 'shell', 'sherd', 'shews', 'shied', 'shier', 'shies', 'shift', 'shiki', 'shill', 'shims', 'shine', 'shins', 
'shiny', 'ships', 'shire', 'shirk', 'shirr', 'shirt', 'shish', 'shits', 'shlep', 'shmoo', 'shnor', 'shoal', 'shoat', 'shock', 'shoed', 'shoer', 'shoes', 'shoji', 'shone', 'shook', 
'shoot', 'shops', 'shore', 'shorn', 'short', 'shots', 'shout', 'shove', 'shown', 'shows', 'showy', 'shred', 'shrew', 'shrub', 'shrug', 'shuck', 'shuns', 'shunt', 'shush', 'shuts', 
'shyer', 'shyly', 'sibyl', 'sicko', 'sicks', 'sided', 'sides', 'sidle', 'siege', 'sieve', 'sifts', 'sighs', 'sight', 'sigma', 'signs', 'silks', 'silky', 'sills', 'silly', 'silos', 
'silts', 'silty', 'since', 'sines', 'sinew', 'singe', 'sings', 'sinks', 'sinus', 'sired', 'siree', 'siren', 'sires', 'sirup', 'sisal', 'sissy', 'sitar', 'sited', 'situs', 'sixes', 
'sixth', 'sixty', 'sized', 'sizer', 'sizes', 'skate', 'skeet', 'skein', 'skews', 'skids', 'skied', 'skier', 'skies', 'skiff', 'skill', 'skimp', 'skims', 'skint', 'skips', 'skirt', 
'skits', 'skoal', 'skulk', 'skull', 'skunk', 'skyed', 'slabs', 'slack', 'slags', 'slain', 'slake', 'slams', 'slang', 'slant', 'slaps', 'slash', 'slate', 'slats', 'slave', 'slaws', 
'slays', 'sleds', 'sleek', 'sleep', 'sleet', 'slept', 'slews', 'slice', 'slick', 'slide', 'slier', 'slily', 'slime', 'slims', 'slimy', 'sling', 'slink', 'slips', 'slits', 'slobs', 
'sloes', 'slogs', 'slomo', 'sloop', 'slope', 'slops', 'slosh', 'sloth', 'slots', 'slows', 'slued', 'slues', 'sluff', 'slugs', 'slump', 'slums', 'slung', 'slunk', 'slurp', 'slurs', 
'slush', 'sluts', 'slyer', 'slyly', 'smack', 'small', 'smart', 'smash', 'smear', 'smell', 'smelt', 'smile', 'smirk', 'smite', 'smith', 'smock', 'smoke', 'smoky', 'smote', 'smurf', 
'smuts', 'snack', 'snafu', 'snags', 'snail', 'snake', 'snaky', 'snaps', 'snare', 'snarf', 'snark', 'snarl', 'sneak', 'sneer', 'snide', 'sniff', 'snipe', 'snips', 'snits', 'snobs', 
'snood', 'snook', 'snoop', 'snoot', 'snore', 'snort', 'snots', 'snout', 'snows', 'snowy', 'snubs', 'snuck', 'snuff', 'snugs', 'soaks', 'soapy', 'soars', 'sober', 'socko', 'socks', 
'socle', 'sodas', 'sofas', 'softs', 'softy', 'soggy', 'soils', 'solar', 'soled', 'soles', 'solid', 'solon', 'solos', 'solum', 'solve', 'somas', 'sonar', 'songs', 'sonic', 'sonly', 
'sonny', 'sooth', 'soots', 'sooty', 'soppy', 'sorer', 'sores', 'sorry', 'sorta', 'sorts', 'souls', 'sound', 'soups', 'soupy', 'souse', 'south', 'sowed', 'sower', 'soyas', 'space', 
'spacy', 'spade', 'spake', 'spang', 'spank', 'spans', 'spare', 'spark', 'spars', 'spasm', 'spate', 'spats', 'spawn', 'spazz', 'speak', 'spear', 'speck', 'specs', 'speed', 'spell', 
'spelt', 'spend', 'spent', 'sperm', 'spews', 'spice', 'spics', 'spicy', 'spied', 'spiel', 'spier', 'spies', 'spike', 'spiky', 'spill', 'spilt', 'spina', 'spine', 'spins', 'spiny', 
'spire', 'spite', 'spits', 'spitz', 'spivs', 'splat', 'splay', 'split', 'spoil', 'spoke', 'spoof', 'spook', 'spool', 'spoon', 'spoor', 'spore', 'sport', 'spots', 'spout', 'sprat', 
'spray', 'spree', 'sprig', 'sprit', 'sprog', 'sprue', 'spuds', 'spued', 'spume', 'spumy', 'spunk', 'spurn', 'spurs', 'spurt', 'sputa', 'squab', 'squad', 'squat', 'squaw', 'squib', 
'squid', 'stabs', 'stack', 'staff', 'stage', 'stags', 'stagy', 'staid', 'stain', 'stair', 'stake', 'stale', 'stalk', 'stall', 'stamp', 'stand', 'stank', 'staph', 'stare', 'stark', 
'stars', 'start', 'stash', 'state', 'stats', 'stave', 'stays', 'stead', 'steak', 'steal', 'steam', 'steed', 'steel', 'steep', 'steer', 'stein', 'stela', 'stele', 'stems', 'steno', 
'steps', 'stern', 'stets', 'stews', 'stick', 'stied', 'sties', 'stiff', 'stile', 'still', 'stilt', 'sting', 'stink', 'stint', 'stirs', 'stoae', 'stoas', 'stoat', 'stock', 'stogy', 
'stoic', 'stoke', 'stole', 'stoma', 'stomp', 'stone', 'stony', 'stood', 'stool', 'stoop', 'stops', 'store', 'stork', 'storm', 'story', 'stoup', 'stout', 'stove', 'stows', 'strap', 
'straw', 'stray', 'strep', 'strew', 'strip', 'strop', 'strum', 'strut', 'stubs', 'stuck', 'studs', 'study', 'stuff', 'stump', 'stung', 'stunk', 'stuns', 'stunt', 'styes', 'style', 
'styli', 'suave', 'sucks', 'sudsy', 'suede', 'suers', 'suets', 'suety', 'sugar', 'suing', 'suite', 'sulfa', 'sulks', 'sulky', 'sully', 'sumac', 'summa', 'sumps', 'sunny', 'sunup', 
'super', 'supes', 'supra', 'suras', 'surds', 'surer', 'surfs', 'surge', 'surly', 'sushi', 'swabs', 'swags', 'swain', 'swami', 'swamp', 'swank', 'swans', 'swaps', 'sward', 'sware', 
'swarf', 'swarm', 'swart', 'swash', 'swath', 'swats', 'sways', 'swear', 'sweat', 'sweep', 'sweet', 'swell', 'swept', 'swift', 'swigs', 'swill', 'swims', 'swine', 'swing', 'swipe', 
'swirl', 'swish', 'swiss', 'swive', 'swoon', 'swoop', 'sword', 'swore', 'sworn', 'swung', 'sylph', 'synch', 'syncs', 'synod', 'syrup', 'tabby', 'table', 'taboo', 'tabor', 'tabus', 
'tacet', 'tacit', 'tacks', 'tacky', 'tacos', 'tacts', 'taels', 'taffy', 'tails', 'taint', 'taken', 'taker', 'takes', 'talcs', 'tales', 'talks', 'talky', 'tally', 'talon', 'talus', 
'tamed', 'tamer', 'tames', 'tamps', 'tango', 'tangs', 'tangy', 'tansy', 'taped', 'taper', 'tapes', 'tapir', 'tapis', 'tardy', 'tared', 'tares', 'tarns', 'taros', 'tarot', 'tarps', 
'tarry', 'tarts', 'tasks', 'taste', 'tasty', 'tater', 'tatty', 'taunt', 'taupe', 'tawny', 'taxed', 'taxer', 'taxes', 'taxis', 'taxol', 'taxon', 'teach', 'teaks', 'teals', 'teams', 
'tears', 'teary', 'tease', 'teats', 'techs', 'techy', 'teddy', 'teems', 'teens', 'teeny', 'teeth', 'telex', 'tells', 'telly', 'tempi', 'tempo', 'temps', 'tempt', 'tench', 'tends', 
'tenet', 'tenon', 'tenor', 'tense', 'tenth', 'tepee', 'tepid', 'terce', 'terms', 'terns', 'terra', 'terry', 'terse', 'tesla', 'tests', 'testy', 'tetra', 'texas', 'texts', 'thane', 
'thank', 'thanx', 'thats', 'thaws', 'theft', 'their', 'theme', 'thens', 'there', 'therm', 'these', 'theta', 'thews', 'thick', 'thief', 'thigh', 'thine', 'thing', 'think', 'thins', 
'third', 'thong', 'thorn', 'those', 'thous', 'three', 'threw', 'throb', 'throe', 'throw', 'thrum', 'thuds', 'thugs', 'thumb', 'thump', 'thunk', 'thwap', 'thyme', 'tiara', 'tibia', 
'ticks', 'tidal', 'tided', 'tiers', 'tiffs', 'tiger', 'tight', 'tikes', 'tikis', 'tilde', 'tiled', 'tiler', 'tiles', 'tills', 'tilth', 'tilts', 'timed', 'timer', 'times', 'timid', 
'tines', 'tinge', 'tinny', 'tints', 'tippy', 'tipsy', 'tired', 'tires', 'tiros', 'titan', 'titer', 'tithe', 'title', 'titre', 'titty', 'tizzy', 'toads', 'toady', 'toast', 'today', 
'toddy', 'toffy', 'togas', 'toile', 'toils', 'toked', 'token', 'toker', 'tokes', 'tolls', 'tombs', 'tomes', 'tommy', 'tonal', 'toned', 'toner', 'tones', 'tonga', 'tongs', 'tonic', 
'tools', 'tooth', 'toots', 'topaz', 'toped', 'toper', 'topes', 'topic', 'topoi', 'topos', 'toque', 'torah', 'torch', 'toric', 'torsi', 'torso', 'torte', 'torts', 'torus', 'total', 
'totem', 'toter', 'totes', 'totty', 'touch', 'tough', 'tours', 'touts', 'toves', 'towed', 'towel', 'tower', 'towns', 'toxic', 'toxin', 'toyed', 'toyer', 'toyon', 'trace', 'track', 
'tract', 'trade', 'trail', 'train', 'trait', 'tramp', 'trams', 'trans', 'traps', 'trash', 'trawl', 'trays', 'tread', 'treap', 'treat', 'treed', 'trees', 'treks', 'trend', 'trews', 
'treys', 'triad', 'trial', 'tribe', 'tribs', 'trice', 'trick', 'tried', 'trier', 'tries', 'trike', 'trill', 'trims', 'trios', 'tripe', 'trips', 'trite', 'troll', 'troop', 'trope', 
'troth', 'trots', 'trout', 'trove', 'trows', 'truce', 'truck', 'trued', 'truer', 'trues', 'truly', 'trump', 'trunk', 'truss', 'trust', 'truth', 'tryst', 'tsars', 'tubal', 'tubas', 
'tubby', 'tubed', 'tuber', 'tubes', 'tucks', 'tufas', 'tufts', 'tufty', 'tulip', 'tulle', 'tummy', 'tumor', 'tunas', 'tuned', 'tuner', 'tunes', 'tunic', 'tuple', 'turbo', 'turds', 
'turdy', 'turfs', 'turfy', 'turns', 'turps', 'tusks', 'tusky', 'tutor', 'tutti', 'tutus', 'tuxes', 'twain', 'twang', 'twats', 'tweak', 'tweed', 'tweet', 'twerp', 'twice', 'twigs', 
'twill', 'twine', 'twink', 'twins', 'twiny', 'twirl', 'twirp', 'twist', 'twits', 'twixt', 'tying', 'tykes', 'typal', 'typed', 'types', 'typos', 'tyros', 'tzars', 'udder', 'ukase', 
'ulcer', 'ulnar', 'ulnas', 'ultra', 'umbel', 'umber', 'umbra', 'umiak', 'umped', 'umpty', 'unapt', 'unarc', 'unarm', 'unary', 'unate', 'unbar', 'unbox', 'uncap', 'uncle', 'uncut', 
'under', 'undid', 'undue', 'unfed', 'unfit', 'unfix', 'unhip', 'unhit', 'unify', 'union', 'unite', 'units', 'unity', 'unjam', 'unlit', 'unman', 'unmap', 'unmet', 'unpeg', 'unpin', 
'unrig', 'unsay', 'unsee', 'unset', 'unsew', 'unsex', 'untie', 'until', 'unwed', 'unwon', 'unzip', 'upend', 'upped', 'upper', 'upset', 'urban', 'ureas', 'urged', 'urger', 'urges', 
'urine', 'usage', 'users', 'usher', 'using', 'usual', 'usurp', 'usury', 'uteri', 'utero', 'utile', 'utter', 'uvula', 'vacua', 'vacuo', 'vague', 'vagus', 'vails', 'vales', 'valet', 
'valid', 'valor', 'value', 'valve', 'vamps', 'vaned', 'vanes', 'vapes', 'vapid', 'vapor', 'varia', 'vases', 'vault', 'vaunt', 'veals', 'veers', 'vegan', 'veils', 'veins', 'veiny', 
'velar', 'velds', 'veldt', 'venal', 'vends', 'venom', 'vents', 'venue', 'verbs', 'verge', 'versa', 'verse', 'verso', 'verst', 'verve', 'vests', 'vetch', 'vexed', 'vexes', 'vials', 
'viand', 'vibes', 'vicar', 'vices', 'video', 'viers', 'views', 'vigil', 'vigor', 'viler', 'villa', 'ville', 'villi', 'vinca', 'vines', 'vinyl', 'viola', 'viols', 'viper', 'viral', 
'vireo', 'vires', 'virus', 'visas', 'vised', 'vises', 'visit', 'visor', 'vista', 'vitae', 'vital', 'vitam', 'vitas', 'vivas', 'vivid', 'vivre', 'vixen', 'vizor', 'vocab', 'vocal', 
'vodka', 'vogue', 'voice', 'voids', 'voila', 'voile', 'volts', 'vomit', 'voted', 'voter', 'votes', 'vouch', 'vowel', 'vower', 'voxel', 'vroom', 'vulva', 'vying', 'wacko', 'wacky', 
'waded', 'wader', 'wades', 'wadis', 'wafer', 'wafts', 'waged', 'wager', 'wages', 'wagon', 'wahoo', 'wails', 'waist', 'waits', 'waive', 'waked', 'waken', 'waker', 'wakes', 'waled', 
'wales', 'walks', 'walls', 'waltz', 'wands', 'waned', 'wanes', 'wanly', 'wanna', 'wanta', 'wards', 'wares', 'warms', 'warns', 'warps', 'warts', 'warty', 'washy', 'wasps', 'waspy', 
'wassa', 'waste', 'watch', 'water', 'watsa', 'watts', 'waved', 'waver', 'waves', 'waxen', 'waxer', 'waxes', 'wazoo', 'weald', 'weals', 'weans', 'wears', 'weary', 'weave', 'webby', 
'weber', 'wedge', 'wedgy', 'weeds', 'weedy', 'weeks', 'weeny', 'weeps', 'weest', 'wefts', 'weigh', 'weird', 'weirs', 'welch', 'welds', 'wells', 'welsh', 'welts', 'wench', 'wends', 
'wests', 'wetly', 'whack', 'whale', 'whams', 'whang', 'wharf', 'wheal', 'wheat', 'wheee', 'wheel', 'whelk', 'whelm', 'whelp', 'whens', 'where', 'whets', 'whews', 'wheys', 'which', 
'whiff', 'while', 'whims', 'whine', 'whiny', 'whips', 'whirl', 'whirr', 'whirs', 'whish', 'whisk', 'whist', 'white', 'whits', 'whizz', 'whoas', 'whole', 'whomp', 'whooo', 'whoop', 
'whops', 'whore', 'whorl', 'whose', 'whoso', 'wicks', 'widen', 'wider', 'widow', 'width', 'wield', 'wifey', 'wight', 'wilco', 'wilds', 'wiled', 'wiles', 'wills', 'willy', 'wilts', 
'wimps', 'wimpy', 'wince', 'winch', 'winds', 'windy', 'wines', 'winey', 'wings', 'winks', 'winos', 'wiped', 'wiper', 'wipes', 'wired', 'wirer', 'wires', 'wised', 'wiser', 'wises', 
'wisps', 'wispy', 'wists', 'witch', 'withs', 'witty', 'wives', 'wizen', 'woken', 'wolds', 'woman', 'wombs', 'women', 'wonks', 'wonky', 'wonts', 'woods', 'woody', 'wooed', 'wooer', 
'woofs', 'wools', 'wooly', 'woosh', 'woozy', 'wordy', 'works', 'world', 'worms', 'wormy', 'worry', 'worse', 'worst', 'worth', 'worts', 'would', 'wound', 'woven', 'wowed', 'wowee', 
'wrack', 'wraps', 'wrath', 'wreak', 'wreck', 'wrens', 'wrest', 'wrier', 'wring', 'wrist', 'write', 'writs', 'wrong', 'wrote', 'wroth', 'wrung', 'wryer', 'wryly', 'wurst', 'xenon', 
'xerox', 'xored', 'xylem', 'yacht', 'yanks', 'yards', 'yarns', 'yawed', 'yawls', 'yawns', 'yawny', 'yawps', 'yearn', 'years', 'yeast', 'yecch', 'yella', 'yells', 'yelps', 'yenta', 
'yerba', 'yeses', 'yield', 'yipes', 'yobbo', 'yodel', 'yogas', 'yogic', 'yogis', 'yoked', 'yokel', 'yokes', 'yolks', 'yolky', 'yores', 'young', 'yourn', 'yours', 'youse', 'youth', 
'yowls', 'yoyos', 'yucky', 'yukky', 'yules', 'yummy', 'yurts', 'zappy', 'zayin', 'zeals', 'zebra', 'zebus', 'zeros', 'zests', 'zesty', 'zetas', 'zilch', 'zincs', 'zings', 'zingy', 
'zippy', 'zombi', 'zonal', 'zoned', 'zones', 'zonks', 'zooey', 'zooks', 'zooms', 'zowie']


df = pd.DataFrame()
df['word'] = words

places = ['one', 'two', 'three', 'four', 'five']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in alpha:
    df[i] = -1
for i in alpha:
    for j, k in enumerate(df['word']):
        if df['word'][j].find(i) == -1:
            df[i][j] = 0
        else:
            df[i][j] = 1

# proportion of most used letters found online - not ideal since it is based on all words regardless of length
# value_dict = {
#     'a': 0.084966, 'b': 0.02072, 'c': 0.045388, 'd': 0.033844, 'e': 0.111607,
#     'f': 0.018121, 'g': 0.024705, 'h': 0.030034, 'i': 0.075448, 'j': 0.001965,
#     'k': 0.011016, 'l': 0.054893, 'm': 0.030129, 'n': 0.066544, 'o': 0.071635,
#     'p': 0.031671, 'q': 0.001962, 'r': 0.075809, 's': 0.057351, 't': 0.069509,
#     'u': 0.036308, 'v': 0.010074, 'w': 0.012899, 'x': 0.002902, 'y': 0.017779, 'z': 0.002722}

# better to pick most likely letters on only 5-letter words, not all words
# give every letter a score based on the count of 5-letter words that contain the letter / the count for all 26 letters
    # I don't really need to divide by the sum of all, I just wanted a ratio based number instead of a raw sum
# this will also bypass giving any more credit to words with a good letter occurring twice
alpha_total = 0
for i in alpha:
    alpha_total += np.sum(df[i])
alpha_total

value_dict = {}
for i in alpha:
    value_dict[i] = np.sum(df[i])/alpha_total
value_dict

# one - five
for j, k in enumerate(places):
    df[k] = df['word'].str[j:j+1]

# one_val - five_val
for j in places:
    df[j + '_val'] = df[j].map(value_dict)

# TODO - this could likely be optimized a lot better. There must be some way to reduce the heavy looping
# how about making more columns, direct x - y and if the output is 0 then it's a match
# 2 to 1
df['two_match'] = -1
for i, v in enumerate(df['word']):
    if df['two_val'][i] == df['one_val'][i]:
        df['two_match'][i] = 0
    else:
        df['two_match'][i] = 1
# 3 to 2-1
df['three_match'] = -1
for i, v in enumerate(df['word']):
    if df['three_val'][i] == df['two_val'][i]:
        df['three_match'][i] = 0
    elif df['three_val'][i] == df['one_val'][i]:
        df['three_match'][i] = 0
    else:
        df['three_match'][i] = 1
# 4 to 3-1
df['four_match'] = -1
for i, v in enumerate(df['word']):
    if df['four_val'][i] == df['three_val'][i]:
        df['four_match'][i] = 0
    elif df['four_val'][i] == df['two_val'][i]:
        df['four_match'][i] = 0
    elif df['four_val'][i] == df['one_val'][i]:
        df['four_match'][i] = 0
    else:
        df['four_match'][i] = 1
# 5 to 4-1
df['five_match'] = -1
for i, v in enumerate(df['word']):
    if df['five_val'][i] == df['four_val'][i]:
        df['five_match'][i] = 0
    elif df['five_val'][i] == df['three_val'][i]:
        df['five_match'][i] = 0
    elif df['five_val'][i] == df['two_val'][i]:
        df['five_match'][i] = 0
    elif df['five_val'][i] == df['one_val'][i]:
        df['five_match'][i] = 0
    else:
        df['five_match'][i] = 1

df['word_score'] = round(df['one_val'] + (df['two_val'] * df['two_match']) + (df['three_val'] * df['three_match']) + (df['four_val'] * df['four_match']) + (df['five_val'] * df['five_match']),4)



# Current directory for Flask app
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(APP_ROOT, 'word_data_created.xlsx')
# df = pd.read_excel(file_path)

# main solver function
def wordle_solver_split(import_df, must_not_be_present: str, 
    present1: str, present2: str, present3: str, present4: str, present5: str,
    not_present1: str, not_present2: str, not_present3: str, not_present4: str, not_present5: str):

    final_out2 = must_not_be_present + present1 + present2 + present3 + present4 + present5 + \
        not_present1 + not_present2 + not_present3 + not_present4 + not_present5

    # split individual letters into lists
    must_not_be_present = list(must_not_be_present)
    present = [present1, present2, present3, present4, present5]
    not_present = [not_present1, not_present2, not_present3, not_present4, not_present5]
    must_be_present = (''.join(not_present))

    places = ['one', 'two', 'three', 'four', 'five']
    # df = pd.read_excel(import_df)
    df = import_df.copy()
    total_len = len(df)

    # process the 'must be present' letters
    for j in must_be_present:
        drop_list = []
        for i in range(len(df)):
            drop_list.append(df['word'][i].find(j))
        df['drop_no_' + j] = drop_list
    for j in must_be_present:
        df = df[df['drop_no_' + j] != -1]

    # process the 'must not be present' letters
    for i in places:
        for j in must_not_be_present:
            df = df[df[i] != j]

    # process the 'specific values must be present' letters
    for i, v in enumerate(places):
        if present[i] != '':
            df = df[df[v] == present[i]]

    # process the 'specific values not must be present' letters
    for j, k in enumerate(places):
        if len(not_present[j]) > 0:
            for i in not_present[j]:
                df = df[df[k] != (','.join(i))]

    # pick the best (aka reasonably good) choice by sorting on the highest 'word_score'
    df = df.sort_values(by = 'word_score', ascending =  False)

    try:
        final_out1 = 'Pick 1: ' + df.iat[0, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out1 = 'No words found'
    try:
        final_out2 = 'Pick 2: ' + df.iat[1, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out2 = ''
    try:
        final_out3 = 'Pick 3: ' + df.iat[2, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out3 = ''
    try:
        final_out4 = 'Pick 4: ' + df.iat[3, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out4 = ''
    try:
        final_out5 = 'Pick 5: ' + df.iat[4, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out5 = ''
    final_out_end = f'Options remaining: {len(df)}/{total_len} ({round(len(df)/total_len*100,2)}%)'

    return final_out1, final_out2, final_out3, final_out4, final_out5, final_out_end

def find_word_with_letters(import_df, must_be_present: str):
    # df = pd.read_excel(import_path)
    df = import_df.copy()

    count_list = []
    for i in range(len(df)):
        counting = 0
        for j in must_be_present:
            if df['word'][i].find(j) == -1:
                counting += 0
            else:
                counting += 1
        count_list.append(counting)
            
    df['char_match_count'] = count_list

    df = df.sort_values(by = ['char_match_count', 'word_score'], ascending =  False)
    df = df[['word', 'char_match_count']]

    try:
        final_out1 = f"Pick 1: {df.iat[0, 0]} ({df['char_match_count'].iloc[0]} match)"
    except:
        final_out1 = 'No words found'
    try:
        final_out2 = f"Pick 2: {df.iat[1, 0]} ({df['char_match_count'].iloc[1]} match)"
    except:
        final_out2 = ''
    try:
        final_out3 = f"Pick 3: {df.iat[2, 0]} ({df['char_match_count'].iloc[2]} match)"
    except:
        final_out3 = ''
    try:
        final_out4 = f"Pick 4: {df.iat[3, 0]} ({df['char_match_count'].iloc[3]} match)"
    except:
        final_out4 = ''
    try:
        final_out5 = f"Pick 5: {df.iat[4, 0]} ({df['char_match_count'].iloc[4]} match)"
    except:
        final_out5 = ''

    return final_out1, final_out2, final_out3, final_out4, final_out5


@app.route("/", methods=["POST", "GET"])
def run_wordle():
    if request.method == "POST":
        must_not_be_present = request.form["must_not_be_present"]
        present1 = request.form["present1"]
        present2 = request.form["present2"]
        present3 = request.form["present3"]
        present4 = request.form["present4"]
        present5 = request.form["present5"]
        not_present1 = request.form["not_present1"]
        not_present2 = request.form["not_present2"]
        not_present3 = request.form["not_present3"]
        not_present4 = request.form["not_present4"]
        not_present5 = request.form["not_present5"]
        final_out1, final_out2, final_out3, final_out4, final_out5, final_out_end = \
            wordle_solver_split(df, must_not_be_present, present1, present2, present3, present4, present5, not_present1, not_present2, not_present3, not_present4, not_present5)
        return render_template("index.html", final_out1=final_out1, final_out2=final_out2, final_out3=final_out3, final_out4=final_out4, final_out5=final_out5, final_out_end=final_out_end, \
            must_not_be_present_val=must_not_be_present, present1_val=present1, present2_val=present2, present3_val=present3, present4_val=present4, present5_val=present5, \
            not_present1_val=not_present1, not_present2_val=not_present2, not_present3_val=not_present3, not_present4_val=not_present4, not_present5_val=not_present5)
    else:
        return render_template("index.html")

@app.route("/fixer", methods=["POST", "GET"])
def run_wordle_fixer():
    if request.method == "POST":
        must_be_present = request.form["must_be_present"]
        final_out1, final_out2, final_out3, final_out4, final_out5 = find_word_with_letters(df, must_be_present)
        return render_template("fixer.html", final_out1=final_out1, final_out2=final_out2, final_out3=final_out3, final_out4=final_out4, final_out5=final_out5, must_be_present=must_be_present)
    else:
        return render_template("fixer.html")




# @app.route('/home')
# def home2():
#     return "Hello! this is the main page <h1>HELLO</h1>"  

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# @app.route('/flask')
# def hello_flask():
#    return "123" + "123,123"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home2"))



if __name__ == "__main__":
    app.run(debug=True)