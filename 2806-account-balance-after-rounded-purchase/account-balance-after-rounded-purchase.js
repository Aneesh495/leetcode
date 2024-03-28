var accountBalanceAfterPurchase = function(purchaseAmount) {
    return 100 - Math.round(purchaseAmount / 10) * 10;
};
