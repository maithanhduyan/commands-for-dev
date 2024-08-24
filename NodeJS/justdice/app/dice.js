const Dice = {};

Dice.get_target = function (chance, roll) {
    chance = parseFloat(chance); // Chuyển đổi thành số trước
    if (roll === "rhigh") {
        return parseFloat((99.999999 - chance).toFixed(7)); // Áp dụng toFixed sau khi tính toán
    }
    return parseFloat(chance.toFixed(7));
};

Dice.calculate_payout = function (chance) {
    const house_edge = 1;
    return parseFloat((100 - house_edge) / chance).toFixed(7);
};

Dice.calculate_profit = function (chance, bet) {
    return parseFloat((Dice.calculate_payout(chance) - 1) * bet).toFixed(7);
};

export default Dice;
