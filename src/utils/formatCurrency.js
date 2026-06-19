/**
 * Format a numeric amount as a localised currency string.
 * @param {number} amount
 * @param {string} currency - ISO 4217 code, e.g. "USD"
 * @param {string} [locale="en-US"]
 * @returns {string}
 */
export function formatCurrency(amount, currency, locale = "en-US") {
  return new Intl.NumberFormat(locale, {
    style: "currency",
    currency,
  }).format(amount);
}

/**
 * Parse a localised currency string back to a number.
 * Strips all non-numeric characters except decimal separators.
 * @param {string} str
 * @returns {number}
 */
export function parseCurrency(str) {
  return parseFloat(str.replace(/[^0-9.-]/g, ""));
}
