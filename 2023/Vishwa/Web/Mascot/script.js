stat = 0;
btn = [
    [],
    [],
    []
];
dict = {
    b0: [0, 0],
    b1: [0, 1],
    b2: [0, 2],
    b3: [1, 0],
    b4: [1, 1],
    b5: [1, 2],
    b6: [2, 0],
    b7: [2, 1],
    b8: [2, 2],
}

for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        btn[i][j] = null;
    }
}

function check(id) {
    stat++;
    let i = dict[id][0];
    let j = dict[id][1];
    let ox = document.querySelector("#" + id);
    if (stat % 2 != 0) {
        value = '<i class="bx bx-lemon"></i>';
        btn[i][j] = true;
    } else {
        value = '<i class="bx bx-popsicle"></i>';
        btn[i][j] = false;
    }

    ox.innerHTML = value;
    ox.setAttribute('disabled', true);

    if (btn[i][0] != null && btn[i][0] == btn[i][1] && btn[i][1] == btn[i][2])
        wins(value);
    else if (btn[0][j] != null && btn[0][j] == btn[1][j] && btn[1][j] == btn[2][j])
        wins(value);
    else if (btn[0][0] != null && btn[0][0] == btn[1][1] && btn[1][1] == btn[2][2] ||
        btn[0][2] != null && btn[0][2] == btn[1][1] && btn[1][1] == btn[2][0])
        wins(value);
    else if (stat >= 9)
        draw();
}

function wins(value) {
    Swal.fire({
        icon: 'success',
        title: 'Player ' + value + ' won!',
        html: 'Hurrey! You are really awesome',
        confirmButtonText: 'Play again'
    }).then(function () {
        window.location.reload();
    })
}

function draw() {
    Swal.fire({
        icon: 'info',
        title: 'Match Draw!',
        html: 'Oops! Please play again',
        confirmButtonText: 'Play again'
    }).then(function () {
        window.location.reload();
    })
}