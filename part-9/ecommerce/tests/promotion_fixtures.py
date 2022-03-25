from datetime import date, timedelta

import pytest
from ecommerce.promotion.models import Coupon, Promotion, PromoType


@pytest.fixture
def single_promotion_type(db):
    promotion_type = PromoType.objects.create(name="default")
    return promotion_type


@pytest.fixture
def coupon(db):
    coupon = Coupon.objects.create(
        name="default",
        coupon_code="1234567879",
    )
    return coupon


@pytest.fixture
def promotion_multi_variant(db, single_sub_product_with_media_and_attributes, single_promotion_type, coupon):
    promotion = Promotion.objects.create(
        name="Default",
        promo_reduction=50,
        is_active=False,
        is_schedule=True,
        promo_type=single_promotion_type,
        coupon=coupon,
        promo_start=date.today(),
        promo_end=date.today() + timedelta(5),
    )

    single_sub_product = single_sub_product_with_media_and_attributes
    promotion.products_on_promotion.add(single_sub_product["inventory"], through_defaults={"promo_price": "100.00"})

    return promotion
