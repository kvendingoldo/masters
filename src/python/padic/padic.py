# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import copy


class PAdic(object):
    seq_len = 1 << 7
    limit = int(seq_len / 3) << 1
    precalculated_primes = (1 << 16)
    is_prime = [False] * precalculated_primes

    PAdic.do_eratosthene_sieve([False] * precalculated_primes, precalculated_primes)

    def __init__(self, number, base, type='SIMPLE'):
        PAdic.check_for_prime(base)

        if type == 'SIMPLE':
            if "/" in str(number):
                numbers = number.split('/')
                result = PAdic(int(numbers[0]), base) / (PAdic(int(numbers[1]), base))
                self.digits = result.digits
                self.order = result.order
                self.base = result.base
            else:
                self.digits = [0] * PAdic.seq_len
                self.base = base

                value = str(number).strip()

                if "." in value:
                    point_at = value.rindex('.')
                else:
                    point_at = -1

                pos_in_string = len(value) - 1
                pos_in_digits = 0

                while pos_in_string >= 0:
                    if pos_in_string == point_at:
                        pos_in_string -= 1
                        continue

                    self.digits[pos_in_digits] = value[pos_in_string]  # - '0'
                    pos_in_string -= 1
                    pos_in_digits += 1

                pos = 0

                while pos < PAdic.seq_len and self.digits[pos] == 0:
                    pos += 1

                order = ''

                if point_at != -1:
                    order = -(len(value) - point_at - 1)

                    if order < 0:
                        offset = min(-order, pos)
                        ind = 0
                        while ind + offset < PAdic.seq_len:
                            self.digits[ind] = self.digits[ind + offset]
                            ind += 1
                        order += offset
                else:
                    if pos == PAdic.seq_len:
                        pos = 0
                    order = pos
                self.order = order
        elif type == 'SEQUENCE':
            sequence = number['sequence']
            order = number['order']
            recalculate_sequence = number['recalculate']

            self.base = base
            self.digits = [0] * PAdic.seq_len
            start_position = 0
            start_in_sequence = 0

            if recalculate_sequence:
                pos = 0
                while pos < len(sequence) and sequence[pos] == 0:
                    pos += 1

                if order > 0:
                    start_in_sequence = pos
                    start_position = order
                elif order < 0 and pos > order:
                    start_position = 0
                    start_in_sequence = pos

            pos_in_sequence = start_in_sequence
            ind = start_position
            while pos_in_sequence < len(sequence) and ind < PAdic.seq_len:

                if int(sequence[pos_in_sequence]) < 0:
                    print("P-adic number cannot be built from sequence that contains negative numbers.")
                elif int(sequence[pos_in_sequence]) >= self.base:
                    print("P-adic number cannot be built from sequence that contains digits that are gt or eq to base")
                self.digits[ind] = sequence[pos_in_sequence]
                ind += 1
                pos_in_sequence += 1
            self.order = order

    def __eq__(self, other):
        return self.order == other.order and self.digits == other.digits

    def __repr__(self):
        result = ''
        one_digit_base = self.base <= 7
        pos = self.limit - 1

        while pos >= 0 and self.digits[pos] == 0:
            pos -= 1

        if pos == -1:
            pos += 1

        suffix = "_" if not one_digit_base else ''

        ind = pos

        while ind >= abs(self.order):
            result = result + str(self.digits[ind]) + suffix
            ind -= 1

        if self.order < 0:
            if not one_digit_base and len(result) > 0:
                result = result[0:len(result) - 1]
            result = result + '.'

        ind = abs(self.order) - 1

        while ind >= 0:
            result = result + str(self.digits[ind]) + suffix
            ind -= 1

        if result[0] == '.':
            result.insert(0, "0")

        if not result.startswith("0."):
            pos = 0

            while pos < len(result) and result[pos] == '0':
                pos += 1

            if pos == len(result):
                pos -= 1

            tmp_len = len(result)
            result = result[pos:tmp_len]

        if not one_digit_base:
            tmp_len = len(result)
            result = result[0:tmp_len - 1]

        return result

    def __str__(self):
        result = ''
        one_digit_base = self.base <= 7
        pos = self.limit - 1

        while pos >= 0 and self.digits[pos] == 0:
            pos -= 1

        if pos == -1:
            pos += 1

        suffix = "_" if not one_digit_base else ''

        ind = pos

        while ind >= abs(self.order):
            result = result + str(self.digits[ind]) + suffix
            ind -= 1

        if self.order < 0:
            if not one_digit_base and len(result) > 0:
                result = result[0:len(result) - 1]
            result = result + '.'

        ind = abs(self.order) - 1

        while ind >= 0:
            result = result + str(self.digits[ind]) + suffix
            ind -= 1

        if result[0] == '.':
            result.insert(0, "0")

        if not result.startswith("0."):
            pos = 0

            while pos < len(result) and result[pos] == '0':
                pos += 1

            if pos == len(result):
                pos -= 1

            tmp_len = len(result)
            result = result[pos:tmp_len]

        if not one_digit_base:
            tmp_len = len(result)
            result = result[0:tmp_len - 1]

        return result

    def get_order(self):
        return self.order

    @staticmethod
    def calculate_order(digits, first_order, second_order, operation):
        order = 0

        if operation == 'ADDITION' or operation == 'SUBTRACTION':
            order = min(first_order, second_order)

        if operation == 'MULTIPLICATION':
            order = first_order + second_order

        if operation == 'DIVISION':
            order = first_order - second_order

        pos = 0

        while pos < PAdic.seq_len and digits[pos] == 0:
            pos += 1

        if pos == PAdic.seq_len:
            return 0

        if 0 <= order < pos:
            order = pos

        if order < 0:
            minimum = min(-order, pos)
            ind = 0
            while ind + minimum < PAdic.seq_len:
                digits[ind] = digits[ind + minimum]
                ind += 1

            order += pos

        return order

    def __mul__(self, other):
        PAdic.check_for_base_equality(self, other)

        result = PAdic({
            'sequence': [0] * PAdic.seq_len,
            'order': 0,
            'recalculate': False
        }, self.base, 'SEQUENCE')

        for ind in range(0, PAdic.seq_len, 1):
            temp = self.multiply_to_integer(self.digits, other.digits[ind])
            adder = PAdic({
                'sequence': temp,
                'order': 0,
                'recalculate': False
            }, self.base, 'SEQUENCE')

            result = result.add_by_offset(adder, ind)

        min_order = min(self.get_order(), other.get_order())
        max_order = max(self.get_order(), other.get_order())

        if min_order < 0 and 0 < max_order:
            pos = 0

            while pos < -min_order and result.digits[pos] == 0:
                pos += 1

            ind = 0
            while ind + pos < PAdic.seq_len:
                result.digits[ind] = result.digits[ind + pos]
                ind += 1
        order = PAdic.calculate_order(result.digits, self.get_order(), other.get_order(), 'MULTIPLICATION')

        return PAdic({
            'sequence': result.digits,
            'order': order,
            'recalculate': False
        }, self.base, 'SEQUENCE')

    def multiply_to_integer(self, number, multiplier):
        to_next = 0
        result = [0] * PAdic.seq_len
        for ind in range(0, len(number), 1):
            next = int(number[ind]) * int(multiplier) + int(to_next)
            to_next = next / self.base
            result[ind] = next % self.base
        return result

    def __sub__(self, other):
        PAdic.check_for_base_equality(self, other)
        actual = None
        digits = [0] * PAdic.seq_len
        have_actual = False

        if other.get_order() < 0 and other.get_order() < self.get_order():
            diff = abs(other.get_order() - min(self.get_order(), 0))

            ind = PAdic.seq_len - 1
            while ind - diff >= 0:
                idx = ind - diff
                digits[ind] = self.digits[idx]
                ind -= 1

            new_order = min(self.get_order(), 0) - diff
            actual = PAdic({
                'sequence': digits,
                'order': new_order,
                'recalculate': True
            }, self.base, 'SEQUENCE')

            have_actual = True

        if not have_actual:
            actual = copy.deepcopy(self)

        if actual.get_order() < 0 and other.get_order() >= 0:
            return actual.subtract_by_offset(other, -actual.get_order())

        if actual.get_order() < 0 or other.get_order() < 0:
            left_operand_order = min(actual.get_order(), 0)
            right_operand_order = min(other.get_order(), 0)
            offset = abs(left_operand_order - right_operand_order)
        else:
            offset = 0

        return actual.subtract_by_offset(other, offset)

    def subtract_by_offset(self, subtracted, offset):
        PAdic.check_for_base_equality(self, subtracted)
        result = [0] * PAdic.seq_len

        for ind in range(0, offset, 1):
            result[ind] = self.digits[ind]

        ind = 0

        while ind + offset < PAdic.seq_len:
            idx = ind + offset
            if int(self.digits[idx]) < int(subtracted.digits[ind]):
                take_one = True
                j = idx + 1

                while j < PAdic.seq_len and take_one:
                    if self.digits[j] == 0:
                        self.digits[j] = self.base - 1
                    else:
                        self.digits[j] -= 1
                        take_one = False
                    j += 1
                self.digits[idx] = int(self.digits[idx]) + int(self.base)
            result[idx] = int(self.digits[idx]) - int(subtracted.digits[ind])

            ind += 1
        order = PAdic.calculate_order(result, self.get_order(), subtracted.get_order(), "SUBTRACTION")

        return PAdic({
            'sequence': result,
            'order': order,
            'recalculate': False
        }, self.base, 'SEQUENCE')

    def __truediv__(self, divisor):
        result = [0] * PAdic.seq_len
        divided_digits = [0] * PAdic.seq_len
        divisor_digits = [0] * PAdic.seq_len
        pos = 0

        while pos < PAdic.seq_len and self.digits[pos] == 0 and divisor.digits[pos] == 0:
            pos += 1

        ind = 0
        while ind + pos < PAdic.seq_len:
            divided_digits[ind] = self.digits[ind + pos]
            divisor_digits[ind] = divisor.digits[ind + pos]
            ind += 1

        divided_order = self.get_order() - pos
        divisor_order = divisor.get_order() - pos

        pos = 0
        while pos < PAdic.seq_len and divisor_digits[pos] == 0:
            pos += 1

        ind = 0
        while ind + pos < PAdic.seq_len:
            divisor_digits[ind] = divisor_digits[ind + pos]
            ind += 1
        divided_order -= pos
        divisor_order -= pos

        if divisor_order < 0 and divisor_order < divided_order:
            diff = min(divided_order, 0) - divisor_order

            ind = PAdic.seq_len
            while ind - diff >= 0:
                idx = ind - diff
                divided_digits[ind] = divided_digits[idx]
                divided_digits[idx] = 0
                ind -= 1
            divided_order += diff
            divisor_order = 0

        divided = PAdic({
            'sequence': divided_digits,
            'order': 0,
            'recalculate': False
        }, self.base, 'SEQUENCE')

        actual_divisor = PAdic({
            'sequence': divisor_digits,
            'order': 0,
            'recalculate': False
        }, self.base, 'SEQUENCE')

        for ind in range(0, PAdic.seq_len, 1):
            digit = self.find_multiplier(divided.digits[ind], actual_divisor.digits[0])

            if digit == -1:
                raise Exception("CALCULATION FAILED")

            tmp = self.multiply_to_integer(actual_divisor.digits, digit)
            result[ind] = digit

            divided = divided.subtract_by_offset(PAdic({
                'sequence': tmp,
                'order': 0,
                'recalculate': True
            }, self.base, 'SEQUENCE'), ind)

        order = PAdic.calculate_order(result, divided_order, divisor_order, 'DIVISION')
        number = {
            'sequence': result,
            'order': order,
            'recalculate': False
        }

        return PAdic(number, self.base, 'SEQUENCE')

    def __pos__(self):
        if self.order < 0:
            return -self
        else:
            return self

    def __neg__(self):
        pos = 0
        sequence = [0] * PAdic.seq_len

        while pos < PAdic.seq_len and self.digits[pos] == 0:
            pos += 1

        if pos < PAdic.seq_len:
            sequence[pos] = self.base - int(self.digits[pos])

        for ind in range(pos + 1, PAdic.seq_len, 1):
            sequence[ind] = self.base - self.digits[ind] - 1

        return PAdic({
            'sequence': sequence,
            'order': self.order,
            'recalculate': False
        }, self.base, 'SEQUENCE')

    def add_by_offset(self, added, offset):
        PAdic.check_for_base_equality(self, added)

        result = [0] * PAdic.seq_len
        to_next = 0

        for ind in range(0, offset, 1):
            result[ind] = self.digits[ind]

        ind = 0
        while ind + offset < PAdic.seq_len:
            next = int(self.digits[ind + offset]) + int(added.digits[ind]) + to_next
            to_next = next / self.base
            result[ind + offset] = int(next) % self.base
            ind += 1

        order = PAdic.calculate_order(result, self.get_order(), added.get_order(), 'ADDITION')

        return PAdic({
            'sequence': result,
            'order': order,
            'recalculate': False
        }, self.base, 'SEQUENCE')

    def __add__(self, added):
        PAdic.check_for_base_equality(self, added)
        if self.order < 0 or added.get_order() < 0:
            left_operand_order = min(self.get_order(), 0)
            right_operand_order = min(added.get_order(), 0)
            diff = left_operand_order - right_operand_order
            offset = abs(diff)

            if diff < 0:
                return self.add_by_offset(added, offset)
            else:
                return added.add_by_offset(self, offset)

        return self.add_by_offset(added, 0)

    def find_multiplier(self, mod, multiplier):
        for ind in range(0, self.base, 1):
            if (int(multiplier) * ind) % self.base == int(mod):
                return ind
        return -1

    @staticmethod
    def do_eratosthene_sieve(is_prime, precalculated_primes):
        is_prime = [True] * precalculated_primes
        is_prime[0] = is_prime[1] = False

        ind = 2

        while ind * ind < precalculated_primes:
            if not is_prime[ind]:
                ind += 1
                continue

            for jnd in range(ind + ind, precalculated_primes, ind):
                is_prime[jnd] = False

            ind += 1
        return is_prime

    @staticmethod
    def check_for_base_equality(first, second):
        are_equal = (first.base == second.base)
        if not are_equal:
            raise Exception("Mathematical operations can be done only with p-adic numbers that have the same base")

    @staticmethod
    def check_for_prime(base):
        if not base < PAdic.precalculated_primes:
            raise Exception(
                "Sorry, "
                + base
                + " is too large number to be a base. Enter a prime number that is less than "
                + PAdic.precalculated_primes
            )
        is_prime_base = base > 1 and PAdic.is_prime[base]
        if is_prime_base:
            raise Exception("Base " + base + " is not prime. Base must be a prime number")
