import math


class PAdic:
    len = 1 << 7
    limit = int(len / 3) << 1

    def __init__(self, number, base, type='SIMPLE'):
        # Padic.check_for_prime(base)
        if type == 'SIMPLE':
            if "/" in str(number):

                numerator = int(str(number).split('/')[0])
                denominator = int(str(number).split('/')[1])

                result = PAdic(numerator, base).divide(PAdic(denominator, base))

                self.digits = result.digits
                self.order = result.order
                self.base = result.base

            else:
                self.digits = [0] * self.len
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

                    # if (!Character.isDigit(value.charAt(posInString))) {
                    #   throw new RuntimeException("There can be only digits in the number, no letters or special symbols except of one floating point");
                    # } else if (value.charAt(posInString) - '0' >= this.base) {
                    #   throw new RuntimeException("P-adic number cannot contain digits that are greater or equal to base.");
                    # }

                    # print(value[pos_in_string])
                    self.digits[pos_in_digits] = value[pos_in_string]  # - '0'

                    pos_in_string -= 1
                    pos_in_digits += 1

                pos = 0

                while pos < self.len and self.digits[pos] == 0:
                    pos += 1

                order = ''

                if point_at != -1:
                    order = -(len(value) - point_at - 1)

                    if order < 0:
                        offset = min(-order, pos)
                        ind = 0
                        while ind + offset < self.len:
                            self.digits[ind] = self.digits[ind + offset]
                            ind += 1
                        order += offset
                else:
                    if pos == PAdic.len:
                        pos = 0
                    order = pos
                self.order = order
        elif type == 'SEQUENCE':
            # PAdic.checkForPrime(base);

            sequence = number['sequence']
            order = number['order']
            recalculate_sequence = number['recalculate']

            self.base = base
            self.digits = [0] * PAdic.len
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
            while pos_in_sequence < len(sequence) and ind < PAdic.len:

                if int(sequence[pos_in_sequence]) < 0:
                    print("P-adic number cannot be built from sequence that contains negative numbers.")
                elif int(sequence[pos_in_sequence]) >= self.base:
                    print("P-adic number cannot be built from sequence that contains digits that are gt or eq to base")
                self.digits[ind] = sequence[pos_in_sequence]
                ind += 1
                pos_in_sequence += 1
            self.order = order

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

        while pos < PAdic.len and digits[pos] == 0:
            pos += 1

        if pos == PAdic.len:
            return 0

        if 0 <= order and order < pos:
            order = pos

        if order < 0:
            minimum = min(-order, pos)
            ind = 0
            while ind + minimum < PAdic.len:
                digits[ind] = digits[ind + minimum]
                ind += 1

            order += pos

        return order

    def multiply_to_integer(self, number, multiplier):
        to_next = 0
        result = [0] * self.len
        for ind in range(0, len(number), 1):
            next = int(number[ind]) * int(multiplier) + int(to_next)
            to_next = next / self.base
            result[ind] = next % self.base
        return result

    def subtract(self, subtracted):
        # PAdic.checkForBaseEquality(this, subtracted);
        actual = None
        digits = [0] * PAdic.len
        haveActual = False

        if subtracted.get_order() < 0 and subtracted.get_order() < self.get_order():
            diff = abs(subtracted.get_order() - min(self.get_order(), 0))

            ind = self.len - 1
            while ind - diff >= 0:
                idx = ind - diff
                digits[ind] = self.digits[idx]
                ind -= 1

            newOrder = min(self.get_order(), 0) - diff
            actual = PAdic({
                'sequence': digits,
                'order': newOrder,
                'recalculate': True
            }, self.base, 'SEQUENCE')

            haveActual = True

        if not haveActual:
            actual = self

        if actual.get_order() < 0 and subtracted.get_order() >= 0:
            return actual.subtract_by_offset(subtracted, -actual.get_order())

        offset = 0

        if actual.get_order() < 0 or subtracted.get_order() < 0:
            leftOperandOrder = min(actual.get_order(), 0)
            rightOperandOrder = min(subtracted.get_order(), 0)
            offset = abs(leftOperandOrder - rightOperandOrder)
        else:
            offset = 0

        return actual.subtract_by_offset(subtracted, offset)

    def subtract_by_offset(self, subtracted, offset):
        # PAdic.checkForBaseEquality(this, subtracted);
        result = [0] * self.len
        takeOne = True

        for ind in range(0, offset, 1):
            result[ind] = self.digits[ind]

        ind = 0

        while ind + offset < self.len:
            idx = ind + offset
            if int(self.digits[idx]) < subtracted.digits[ind]:
                takeOne = True
                j = idx + 1

                while j < self.len and takeOne:
                    if self.digits[j] == 0:
                        self.digits[j] = self.base - 1
                    else:
                        self.digits[j] -= 1
                        takeOne = False
                    j += 1
                self.digits[idx] += self.base
            result[idx] = int(self.digits[idx]) - subtracted.digits[ind]

            ind += 1
        order = PAdic.calculate_order(result, self.get_order(), subtracted.get_order(), "SUBTRACTION")

        return PAdic({
            'sequence': result,
            'order': order,
            'recalculate': False
        }, self.base, 'SEQUENCE')

    def divide(self, divisor):
        result = [0] * self.len
        divided_digits = [0] * self.len
        divisor_digits = [0] * self.len
        pos = 0

        while pos < self.len and self.digits[pos] == 0 and divisor.digits[pos] == 0:
            pos += 1

        ind = 0
        while ind + pos < self.len:
            divided_digits[ind] = self.digits[ind + pos]
            divisor_digits[ind] = divisor.digits[ind + pos]
            ind += 1

        divided_order = self.get_order() - pos
        divisor_order = divisor.get_order() - pos

        pos = 0
        while pos < self.len and divisor_digits[pos] == 0:
            pos += 1

        ind = 0
        while ind + pos < self.len:
            divisor_digits[ind] = divisor_digits[ind + pos]
            ind += 1
        divided_order -= pos
        divisor_order -= pos

        if divisor_order < 0 and divisor_order < divided_order:
            diff = min(divided_order, 0) - divisor_order

            ind = self.len
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

        for ind in range(0, self.len, 1):
            digit = self.find_multiplier(divided.digits[ind], actual_divisor.digits[0])

            # if (digit == -1) {
            #    throw new RuntimeException("CALCULATION FAILED. Couldn't find multiplier x satisfying " + divided.digits[i] + " = x" + actualDivisor.digits[0] + " (mod " + this.base + ").");
            # }

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

    def negative(self):
        pos = 0
        sequence = [0] * self.len

        while pos < PAdic.len and self.digits[pos] == 0:
            pos += 1

        if pos < PAdic.len:
            sequence[pos] = self.base - self.digits[pos]

        for ind in range(pos + 1, PAdic.len, 1):
            sequence[ind] = self.base - self.digits[ind] - 1

        return PAdic(sequence, self.order, self.base)

    def add_by_offset(self, added, offset):
        # PAdic.checkForBaseEquality(this, added);

        result = [0] * PAdic.len
        to_next = 0

        for ind in range(0, offset, 1):
            result[ind] = self.digits[ind]

        ind = 0
        while ind + offset < PAdic.len:
            next = int(self.digits[ind + offset]) + added.digits[ind] + to_next
            to_next = next / self.base
            result[ind + offset] = next % self.base
            ind += 1

        order = PAdic.calculate_order(result, self.get_order(), added.get_order(), 'ADDITION')
        print(order)
        return PAdic({
            'sequence': result,
            'order': order,
            'recalculate': False
        }, self.base, 'SEQUENCE')

    def add(self, added):
        # PAdic.checkForBaseEquality(this, added);
        if self.order < 0 or added.get_order() < 0:
            print("test")
            left_operand_order = min(self.get_order(), 0)
            right_operand_order = min(added.get_order(), 0)
            diff = left_operand_order - right_operand_order
            offset = abs(diff)

            if diff < 0:
                return self.add_by_offset(added, offset)
            else:
                return added.add_by_offset(self, offset)

        return self.add_by_offset(added, 0)

    @staticmethod
    def check_for_prime(self):
        pass

    def find_multiplier(self, mod, multiplier):
        for ind in range(0, self.base, 1):
            if (int(multiplier) * ind) % self.base == int(mod):
                return ind
        return -1
