

// Nested Objects

let person = {
    Name: `Matt`,
    Age: 45,
    Position: `John's Supervisor`,
    Title: `The Great Gatsby`,
    Address: {
        City: `London`,
        Country: `England`
    },
    Films: {
        1: {
            FilmName: `The Golden Compass`,
            Genre: `Fantasy, Adventure, Novel, Children Literature`,
            Release: 2007,
            Ratings: 4.3,
        },
        2: {
            FilmName: `Game of Thrones`,
            Genre: `Serial, Action, Drama, Romance, Thriller`,
            Release: 2011,
            Ratings: 4.7,
        },
        3: {
            FilmName: `Harry Potter`,
            Genre: `Fantasy, Novel, Drama`,
            Release: 2001,
            Ratings: 4.8,
        }
    },
    Introduction: function () {
        let string = `${this.Name} is ${this.Age} years old, and lives in ${this.Address.City}`;
        return string;
    },

    PickFilm: function (filmnumber) {
        let filmpick = this.Films[filmnumber];
        if (filmpick != null) {
            let string = `${this.Name} Enjoys watching ${filmpick.FilmName} Released in ${filmpick.Release}. This Film genre is: ${filmpick.Genre}. Has a rating of ${filmpick.Ratings} out of 5.`;
            return string
        }
        else {
            return `number is out of bounds`
        }
    }
}

console.log(person.Name);
console.log(person.Title);

console.log(`Name: `, person.Name, `, Age: `, person.Age, `, City: `, person.Address.City)
console.log(person.Introduction());
console.log(person.PickFilm(1));