// https://refactoring.guru/design-patterns/singleton

class Singleton {
    private static instance: Singleton

    private constructor() {}

    public static getInstance(): Singleton {
        if (!Singleton.instance) Singleton.instance = new Singleton()

        return Singleton.instance
    }

    public someBusinessLogic() {}
}

function clientCode() {
    const s1 = Singleton.getInstance()
    const s2 = Singleton.getInstance()

    if (s1 === s2)
        return console.log(
            'Singleton works, both variables contain the same instance.'
        )

    console.log('Singleton failed, variables contain different instances.')
}

clientCode()
