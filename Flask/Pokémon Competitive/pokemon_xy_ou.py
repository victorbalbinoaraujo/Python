from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/amoongus')
def amoonguss():
    return jsonify({
    'Amoonguss' : {
        'Natures' : ['Bold'],
        'Items' : ['Black Sludge'],
        'Types' : ['Grass', 'Poison'],
        'Abilities' : ['Regenerator'],
        'Moves' : ['Spore', 'Giga Drain', 'Clear Smog', 'Stun Spore', 'Hidden Power Fire', 'Sludge Bomb'],
        'Base Stats' : {
            'HP' : 114,
            'Attack' : 85,
            'Defense' : 70,
            'Sp. Atk' : 85,
            'Sp. Def' : 80,
            'Speed' : 30
        },
        'EVs' : {
            'HP' : 248,
            'Attack' : 0,
            'Defense' : 168,
            'Sp. Atk' : 0,
            'Sp. Def' : 92,
            'Speed' : 0
        }
    }
})

@app.route('/azelf')
def azelf():
    return jsonify({
    'Azelf' : {
        'Natures' : ['Naive'],
        'Items' : ['Focus Sash'],
        'Types' : ['Psychic'],
        'Abilities' : ['Levitate'],
        'Moves' : ['Stealth Rock', 'Explosion', 'Skill Swap', 'Hidden Power Steel', 'Iron Tail', 'Taunt'],
        'Base Stats' : {
            'HP' : 75,
            'Attack' : 125,
            'Defense' : 70,
            'Sp. Atk' : 125,
            'Sp. Def' : 70,
            'Speed' : 115
        },
        'EVs' : {
            'HP' : 0,
            'Attack' : 0,
            'Defense' : 228,
            'Sp. Atk' : 28,
            'Sp. Def' : 0,
            'Speed' : 252
        }
    }
})

@app.route('/azumarill')
def azumarill():
    return jsonify({
    'Azumarill' : {
        'Natures' : ['Adamant'],
        'Items' : ['Choice Band', 'Sitrus Berry', 'Assault Vest'],
        'Types' : ['Water', 'Fairy'],
        'Abilities' : ['Huge Power'],
        'Moves' : ['Play Rough', 'Waterfall', 'Aqua Jet', 'Superpower', 'Knock Off', 'Belly Drum'],
        'Base Stats' : {
            'HP' : 100,
            'Attack' : 50,
            'Defense' : 80,
            'Sp. Atk' : 60,
            'Sp. Def' : 80,
            'Speed' : 50
        },
        'EVs' : {
            'HP' : [172, 92, 240],
            'Attack' : 252,
            'Defense' : 168,
            'Sp. Atk' : 0,
            'Sp. Def' : [0, 16],
            'Speed' : [84, 164]
        }
    }
})
        
@app.route('/bisharp')
def bisharp():
    return jsonify({
    'Bisharp' : {
        'Natures' : ['Adamant', 'Jolly'],
        'Items' : ['Life Orb', 'Black Glasses', 'Lum Berry'],
        'Types' : ['Dark', 'Steel'],
        'Abilities' : ['Defiant'],
        'Moves' : ['Knock Off', 'Swords Dance', 'Iron Head', 'Sucker Punch'],
        'Base Stats' : {
            'HP' : 65,
            'Attack' : 125,
            'Defense' : 100,
            'Sp. Atk' : 60,
            'Sp. Def' : 70,
            'Speed' : 70
        },
        'EVs' : {
            'HP' : 0,
            'Attack' : 252,
            'Defense' : 4,
            'Sp. Atk' : 0,
            'Sp. Def' : 0,
            'Speed' : 252
        }
    }
}) 
    
@app.route('/breelom')
def breelom():
    return jsonify({
    'Breelom' : {
        'Natures' : ['Adamant', 'Jolly'],
        'Items' : ['Life Orb', 'Toxic Orb'],
        'Types' : ['Grass', 'Fighting'],
        'Abilities' : ['Technician', 'Poison Heal'],
        'Moves' : ['Spore', 'Bullet Seed', 'Mach Punch', 'Swords Dance', 'Focus Punch', 'Rock Tomb', 'Superpower', 'Drain Punch', 'Seed Bomb', 'Facade'],
        'Base Stats' : {
            'HP' : 60,
            'Attack' : 130,
            'Defense' : 80,
            'Sp. Atk' : 60,
            'Sp. Def' : 60,
            'Speed' : 70
        },
        'EVs' : {
            'HP' : [0, 12],
            'Attack' : [252, 244],
            'Defense' : [0, 4],
            'Sp. Atk' : 0,
            'Sp. Def' : 0,
            'Speed' : 252
        }
    }
}) 

@app.route('/chansey')
def chansey():
    return jsonify({
    'Chansey' : {
        'Natures' : ['Bold'],
        'Items' : ['Eviolite'],
        'Types' : ['Normal'],
        'Abilities' : ['Natural Cure'],
        'Moves' : ['Toxic', 'Thunder Wave', 'Soft-Boiled', 'Seismic Toss', 'Heal Bell', 'Stealth Rock'],
        'Base Stats' : {
            'HP' : 250,
            'Attack' : 5,
            'Defense' : 5,
            'Sp. Atk' : 35,
            'Sp. Def' : 105,
            'Speed' : 50
        },
        'EVs' : {
            'HP' : 4,
            'Attack' : 0,
            'Defense' : 252,
            'Sp. Atk' : 0,
            'Sp. Def' : 252,
            'Speed' : 0
        }
    }
})
        
app.route('/charizardx')
def charizard_x():
    return jsonify({
    'Charizard X' : {
        'Natures' : ['Adamant', 'Jolly'],
        'Items' : ['Charizardite X'],
        'Types' : ['Fire', 'Dragon'],
        'Abilities' : ['Blaze -> Tough Claws'],
        'Moves' : ['Dragon Dance', 'Flare Blitz', 'Dragon Claw', 'Roost'],
        'Base Stats' : {
            'HP' : 78,
            'Attack' : 130,
            'Defense' : 111,
            'Sp. Atk' : 130,
            'Sp. Def' : 85,
            'Speed' : 100
        },
        'EVs' : {
            'HP' : 0,
            'Attack' : 252,
            'Defense' : 4,
            'Sp. Atk' : 0,
            'Sp. Def' : 0,
            'Speed' : 252
        }
    }
})

app.route('/charizardy')
def charizard_y():
    return jsonify({
    'Charizard Y' : {
        'Natures' : ['Timid', 'Modest'],
        'Items' : ['Charizardite Y'],
        'Types' : ['Fire', 'Flying'],
        'Abilities' : ['Blaze -> Drought'],
        'Moves' : ['Fire Blast', 'Flamethrower', 'Solar Beam', 'Focus Blast', 'Roost'],
        'Base Stats' : {
            'HP' : 78,
            'Attack' : 104,
            'Defense' : 78,
            'Sp. Atk' : 159,
            'Sp. Def' : 115,
            'Speed' : 100
        },
        'EVs' : {
            'HP' : 0,
            'Attack' : 0,
            'Defense' : 0,
            'Sp. Atk' : 252,
            'Sp. Def' : 4,
            'Speed' : 252
        }
    }
})

app.route('/clefable')
def clefable():
    return jsonify({
    'Clefable' : {
        'Natures' : ['Bold', 'Modest'],
        'Items' : ['Leftovers', 'Life Orb'],
        'Types' : ['Fairy'],
        'Abilities' : ['Magic Guard'],
        'Moves' : ['Calm Mind', 'Moonblast', 'Flamethrower', 'Ice Beam', 'Thunder Wave', 'Soft-Boiled', 'Stealth Rock', 'Knock Off'],
        'Base Stats' : {
            'HP' : 95,
            'Attack' : 70,
            'Defense' : 73,
            'Sp. Atk' : 95,
            'Sp. Def' : 90,
            'Speed' : 60
        },
        'EVs' : {
            'HP' : [252, 248],
            'Attack' : 0,
            'Defense' : [252, 236, 172],
            'Sp. Atk' : [0, 72],
            'Sp. Def' : [4, 24, 0],
            'Speed' : [0, 12]
        }
    }
})

app.route('/diancie-mega')
def diancie_mega():
    return jsonify({
    'Diance Mega' : {
        'Natures' : ['Naive', 'Rash'],
        'Items' : ['Diancite'],
        'Types' : ['Rock', 'Fairy'],
        'Abilities' : ['Clear Body -> Magic Bounce'],
        'Moves' : ['Diamond Storm', 'Moonblast', 'Hidden Power Fire', 'Earth Power', 'Protect', 'Rock Polish'],
        'Base Stats' : {
            'HP' : 50,
            'Attack' : 160,
            'Defense' : 110,
            'Sp. Atk' : 160,
            'Sp. Def' : 110,
            'Speed' : 110
        },
        'EVs' : {
            'HP' : [0, 36],
            'Attack' : [8, 32],
            'Defense' : 0,
            'Sp. Atk' : [248, 252],
            'Sp. Def' : 0,
            'Speed' : [252, 188]
        }
    }
})
    
app.route('/dragonite')
def dragonite():
    return jsonify({
    'Dragonite' : {
        'Natures' : ['Adamant', 'Jolly'],
        'Items' : ['Leftovers', 'Lum Berry', 'Choice Band'],
        'Types' : ['Dragon', 'Flying'],
        'Abilities' : ['Multiscale'],
        'Moves' : ['Dragon Dance', 'Substitute', 'Roost', 'Fly', 'Outrage', 'Extreme Speed', 'Earthquake', 'Fire Punch'],
        'Base Stats' : {
            'HP' : 91,
            'Attack' : 134,
            'Defense' : 95,
            'Sp. Atk' : 100,
            'Sp. Def' : 100,
            'Speed' : 80
        },
        'EVs' : {
            'HP' : [252, 0],
            'Attack' : [0, 252],
            'Defense' : [116, 4],
            'Sp. Atk' : 0,
            'Sp. Def' : 0,
            'Speed' : [252, 140]
        }
    }
})
    
app.route('/dugtrio')
def dragonite():
    return jsonify({
    'Dugtrio' : {
        'Natures' : ['Jolly'],
        'Items' : ['Focus Sash'],
        'Types' : ['Ground'],
        'Abilities' : ['Sand Force'],
        'Moves' : ['Stealth Rock', 'Memento', 'Earthquake', 'Toxic', 'Stone Edge'],
        'Base Stats' : {
            'HP' : 35,
            'Attack' : 80,
            'Defense' : 50,
            'Sp. Atk' : 50,
            'Sp. Def' : 70,
            'Speed' : 120
        },
        'EVs' : {
            'HP' : 0,
            'Attack' : 252,
            'Defense' : 4,
            'Sp. Atk' : 0,
            'Sp. Def' : 0,
            'Speed' : 252
        }
    }
})
    
app.route('/excadrill')
def dragonite():
    return jsonify({
    'Excadrill' : {
        'Natures' : ['Adamant', 'Jolly', 'Careful'],
        'Items' : ['Leftovers', 'Life Orb', 'Choice Scarf'],
        'Types' : ['Ground', 'Steel'],
        'Abilities' : ['Sand Rush', 'Mold Breaker'],
        'Moves' : ['Earthquake', 'Iron Head', 'Rapid Spin', 'Swords Dance', 'Rock Slide', 'Toxic'],
        'Base Stats' : {
            'HP' : 110,
            'Attack' : 135,
            'Defense' : 60,
            'Sp. Atk' : 50,
            'Sp. Def' : 65,
            'Speed' : 88
        },
        'EVs' : {
            'HP' : 0,
            'Attack' : 252,
            'Defense' : 4,
            'Sp. Atk' : 0,
            'Sp. Def' : 0,
            'Speed' : 252
        }
    }
})

if __name__ == '__main__':
    app.run(debug=True)