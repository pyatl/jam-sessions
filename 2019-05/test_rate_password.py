
from rate_password import length_score, is_common, complexity_score, rate_password


class TestLengthScore:

    def test_length_good(self):
        assert length_score('password') == 1
        assert length_score('password1234') == 5
    
    def test_too_short(self):
        assert length_score('passwrd') == 0
        assert length_score('foo') == 0
    
    def test_empty(self):
        assert length_score('') == 0
    
    def test_unicode(self):
        assert length_score('Wasserschloß') == 5


class TestIsCommon:

    def test_common(self):
        assert is_common('password') is True
        assert is_common('Password') is True
        assert is_common('qwertyuiop') is True
        assert is_common('security') is True
        assert is_common('spiderma') is True
        assert is_common('123123123') is True

    def test_uncommon(self):
        assert is_common('mu9Emiej') is False
        assert is_common('Keru1nuM') is False
        assert is_common('aic4peeV') is False
        assert is_common('aNaeth6i') is False


class TestComplexityScore:

    def test_lowest_score(self):
        assert complexity_score('password') == 1
        assert complexity_score('qwertyuiop') == 1
    
    def test_mixed_case(self):
        assert complexity_score('hello') == 1
        assert complexity_score('HELLO') == 1
        assert complexity_score('hELlO') == 2
    
    def test_numbers(self):
        assert complexity_score('pass123word') == 3
        assert complexity_score('q1w2e3r4t5') == 3
        assert complexity_score('pass1word') == 2
        
    def test_symbols(self):
        assert complexity_score('pass$#word') == 3
        assert complexity_score('q\'w"e%r&t>') == 3
        assert complexity_score('pass$word') == 2
    
    def test_spaces(self):
        assert complexity_score('hello beautiful world') == 3
        assert complexity_score('hello world') == 2
    
    def test_symbols_numbers_end(self):
        assert complexity_score('password1') == 2
        assert complexity_score('password1234') == 2
        assert complexity_score('password!') == 2
        assert complexity_score('password1!') == 2
        assert complexity_score('PaSsWoRd1234!@#%') == 2
    
    def test_foreign_characters(self):
        assert complexity_score('wasserschloß') == 2  # At the end
        assert complexity_score('waſſerſchloſs') == 4
        assert complexity_score('pass\u0be7word') == 3
        assert complexity_score('pass\u0be7\u0be8\u0be9word') == 4

    def test_various_examples(self):
        assert complexity_score('H3LLO_WORLD') == 3
        assert complexity_score('nen9aPhu') == 3
        assert complexity_score('Ba$th5to') == 4
        assert complexity_score('Dre1käse') == 5
        assert complexity_score('Oo7,28=r+MU}') == 6


class TestRatePassword:

    def test_unacceptable(self):
        # Common passwords
        assert rate_password('password') == 'unacceptable' 
        assert rate_password('q1w2e3r4t5') == 'unacceptable'
        # Too short
        assert rate_password('dai_V5a') == 'unacceptable'
        # 3 for length * 2 for complexity = 6 pts
        assert rate_password('IAmJohnDoe') == 'unacceptable'
        # 4 for length * 2 for complexity = 8 pts 
        assert rate_password('Password12!') == 'unacceptable'

    def test_weak(self):
        # 3 for length * 5 for complexity = 15 pts
        assert rate_password('2A"$hXNl,t') == 'weak'
        # 5 for length * 4 for complexity = 20 pts
        assert rate_password('aen0okoh.l6h') == 'weak'

    def test_ok(self):
        # 7 for length * 4 for complexity = 28 pts
        assert rate_password('Wah4siel4ae0Sh') == 'ok'
        # 9 for length * 5 for complexity = 45 pts
        assert rate_password('ohr5mei!CaigieR2') == 'ok'

    def test_strong(self):
        # 21 for length * 3 for complexity = 63 pts
        assert rate_password('correct horse battery staple') == 'strong'
        # 10 for length * 7 for complexity = 70 pts
        assert rate_password('Ein weißes Pferd!') == 'strong'
        # 13 for length * 6 for complexity = 78 pts
        assert rate_password('loosh6Aikie\'phee-lu3') == 'strong'

