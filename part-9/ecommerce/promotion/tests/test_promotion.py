from ecommerce.promotion.models import Promotion


def test_single_promotion(promotion_multi_variant):
    new_promotion = promotion_multi_variant
    get_promotion = Promotion.objects.all().first()
    assert new_promotion.id == get_promotion.id
    assert new_promotion.coupon.coupon_code == get_promotion.coupon.coupon_code
