from lettuce import step, world


@step("I set name of google photo album")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: Given I set name of google photo album')


@step("I set destination folder")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: And I set destination folder')


@step("I set path ot original photos")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: And I set path ot original photos')


@step("I make request")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: When I make request')


@step("I see all album photos at destination folder in original quality")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: Then I see all album photos at destination folder in original quality')