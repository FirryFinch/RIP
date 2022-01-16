class Urls {
    constructor() {
        this.url = 'http://localhost:8000/';
    }

    stocks() {
        return `${this.url}movies/`
    }

    stock(id) {
        return `${this.url}movies/${id}/`
    }
}

export const urls = new Urls()