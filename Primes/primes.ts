// Online Typescript Editor for free
// Write, Edit and Run your Typescript code using TS Online Compiler

function isPrime(n: number): boolean {
    if (n <= 1) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

if(isPrime(5)) {
    console.log("Es primo")
} else {
    console.log("No es primo")
}
