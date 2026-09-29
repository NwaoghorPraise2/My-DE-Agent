"""
w01-p01 · parse-price
===============================================================================
PROBLEM
Write `parse_price(raw: str) -> Decimal` handling:
- currency symbol ('£1,234.56')
- thousands separators
- plain numbers
- leading/trailing whitespace
- parentheses-negative ('(12.50)' -> -12.50)
- empty/whitespace-only -> ValueError
- any other invalid input after cleaning -> ValueError

Required steps 1-4 (Understand, Example, Approach, Structures & complexity)
before any code.

CONSTRAINTS
- Return type is Decimal, exact to the penny — never go through float
- Invalid input raises ValueError (not InvalidOperation, not a silent None)

EXAMPLE
in:  ' £1,234.56 '  -> Decimal('1234.56')
in:  '(12.50)'      -> Decimal('-12.50')
in:  '   '          -> ValueError

EDGE CASES GIVEN
- empty string / whitespace-only
- parentheses-negative
- garbage after cleaning (e.g. 'abc', '£')

-------------------------------------------------------------------------------
MODE: default          DATE: 2026-09-12 (resumed 2026-09-29)
TIME LIMIT: none       TAKEN: —           HINTS USED: 0
VERDICT: partial — works on every stated case; silent-acceptance gaps open

PLAN (his steps 1-4)
strip -> empty check -> parentheses flag + strip -> remove '£' and ',' ->
Decimal(cleaned) in try/except -> ValueError on failure -> apply sign.
O(n) in string length, string methods only, no regex, no loops.

FIRST ATTEMPT WENT WRONG BY
Plan used a bare `except:` around Decimal(). Corrected to catch
decimal.InvalidOperation specifically so unrelated bugs aren't swallowed.

REVIEW (coach, 2026-09-29) — all 10 of his tests pass. Probed further:
  '(-12.50)' -> Decimal('12.50')   double negative silently flips sign
  '1,23'     -> Decimal('123')     comma position never validated (100x error
                                   if source uses decimal comma)
  '1,2,3'    -> Decimal('123')
  '12.505'   -> Decimal('12.505')  sub-penny accepted, spec said "to the penny"
  '1e3'      -> Decimal('1E+3')    scientific notation accepted
  '1_000'    -> Decimal('1000')    Decimal accepts underscores
  '12£','££12' -> 12               symbol accepted anywhere, any count
  '١٢'       -> Decimal('12')      Decimal accepts non-ASCII digits
Good: is_finite() check (NaN/Infinity) — not asked for, he found it.
Good: 'from exc' chaining; specific InvalidOperation catch.
Tests gap: assertEqual can't see scale — Decimal('12.5') == Decimal('12.50').
Theme: the function REJECTS well but ACCEPTS too much. Validate shape, don't
just strip characters and hope Decimal complains.

CONNECTS TO
Week 1 float vs Decimal vs NUMERIC vs INT-pence (turns 1-4)
===============================================================================
"""

from decimal import Decimal, InvalidOperation


def parse_price(amount: str) -> Decimal:
    """Parse a raw price string into a Decimal."""
    cleaned = amount.strip()

    if not cleaned:
        raise ValueError("Prices Cannot be empty")

    is_negative = False
    if cleaned.startswith("(") or cleaned.endswith(")"):
        if not (cleaned.startswith("(") and cleaned.endswith(")")):
            raise ValueError("Unbalanced parentheses")
        is_negative = True
        cleaned = cleaned[1:-1].strip()

    cleaned = cleaned.replace("£", "").replace(",", "")
    if not cleaned:
        raise ValueError("Invalid price format")

    try:
        value = Decimal(cleaned)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid price format: {exc}") from exc

    if not value.is_finite():
        raise ValueError("Invalid price format: non-finite value")

    if is_negative:
        value = -value

    return value


# --- tests ---------------------------------------------------------------
import unittest


class TestParsePrice(unittest.TestCase):

    def test_normal_number(self):
        self.assertEqual(parse_price("1234.56"), Decimal("1234.56"))

    def test_currency_symbol(self):
        self.assertEqual(parse_price("£1,234.56"), Decimal("1234.56"))

    def test_thousands_separator(self):
        self.assertEqual(parse_price("1,234,567.89"), Decimal("1234567.89"))

    def test_whitespace(self):
        self.assertEqual(parse_price("  99.99  "), Decimal("99.99"))

    def test_parentheses_negative(self):
        self.assertEqual(parse_price("(12.50)"), Decimal("-12.50"))

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            parse_price("")

    def test_whitespace_only(self):
        with self.assertRaises(ValueError):
            parse_price("   ")

    def test_garbage_input(self):
        with self.assertRaises(ValueError):
            parse_price("hello")

    def test_unbalanced_parentheses(self):
        with self.assertRaises(ValueError):
            parse_price("12.50)")

    def test_combined_formatting(self):
        self.assertEqual(parse_price("(£1,234.56)"), Decimal("-1234.56"))


if __name__ == "__main__":
    unittest.main()
