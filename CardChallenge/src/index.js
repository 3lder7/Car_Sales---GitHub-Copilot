/* 
Visa = Começa sempre com 4
# MasterCard = Começa com dígitos entre 51 e 55, ou entre 2221 e 2720
# Elo = Pode começar com vários intervalos, como 4011, 4312, 4389, entre outros.
# American Express = Começa com 34 ou 37
# Discover = Começa com 6011, 65, ou com a faixa de 644 a 649
# HiperCard = Geralmente começa com 6062

Analisar a bandeira do cartão é importante para saber se é permitido um bônus ou não
*/

//ATIVIDADE: Faltam Dinners Club, JCB, Aura, Voyager, Enrout
const cardTypes = {
    Visa: /^4/,
    MasterCard: /^(5[1-5]|222[1-9]|22[3-9]\d|2[3-6]\d{2}|27[01]\d|2720)/,
    Elo: /^(4011|4312|4389)/,
    AmericanExpress: /^3[47]/,
    Discover: /^(6011|65|64[4-9])/,
    HiperCard: /^6062/,
    DinersClub: /^(36|38|30[0-5])/,
    JCB: /^(352[8-9]|35[3-8][0-9])/,
    Aura: /^50[0-9]{14,17}/,
    Voyager: /^8699/,
    Enroute: /^(2014|2149)/
};

function luhnAlgorithm(cardNumber) {
    let sum = 0;
    let shouldDouble = false;
    for (let i = cardNumber.length - 1; i >= 0; i--) {
        let digit = parseInt(cardNumber[i]);
        if (shouldDouble) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        shouldDouble = !shouldDouble;
    }
    return sum % 10 === 0;
}

function getCardType(cardNumber) {
    const cardNumberStr = cardNumber.toString();

    if (!luhnAlgorithm(cardNumberStr)) {
        return 'Invalid card number';
    }

    for (const [cardType, regex] of Object.entries(cardTypes)) {
        if (regex.test(cardNumberStr)) {
            return cardType;
        }
    }

    return 'Unknown';
}

// Example usage
console.log(getCardType(4111111111111111)); // Visa