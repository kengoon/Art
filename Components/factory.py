from kivy.factory import Factory

register = Factory.register


def register_factory():
    register("Blur", module="Components.effectwidget")
    register("Separator", module="Components.separator")
    register("Card", module="Components.card")
    register("Dot", module="Components.dot")
    register("DotSpinner", module="Components.spinner")
    register("TextField", module="Components.textfield")
    register("Navigator", module="Components.navigator")
    register("BoxIconButton", module="Components.navigator")
    register("RecycleContent", module="Components.recycle")
    register("RecycleTask", module="Components.recycle")
    register("RecycleBeggar", module="Components.recycle")
    register("RoundImageButton", module="Components.button")
    register("ToolBar", module="Components.toolbar")
    register("ImageButtonToolbar", module="Components.toolbar")
    register("OutlineIconButton", module="Components.button")
    register("TagTextField", module="Components.textfield")
    register("RaisedButton", module="Components.button")
    register("OutlineImageButton", module="Components.button")
    register("ImageFrame", module="Components.frame")
    register("ListButton", module="Components.button")
    register("StencilBehavior", module="kivymd.uix.behaviors")
    register("ImageCard", module="Components.frame")
    register("IconButton", module="Components.button")
    register("StencilCard", module="Components.card")
    register("BottomNavigationButton", module="Components.button")
    register("RealRecycleView", module="Components.scrollview")
    register("TextFrame", module="Components.frame")
