import builtins
import typing

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gio


class Pixbuf(GObject.Object, Gio.Icon, Gio.LoadableIcon):
    class _Props:
        @property
        def bits_per_sample(self) -> int: ...

        @property
        def has_alpha(self) -> bool: ...

        @property
        def height(self) -> int: ...

        @property
        def n_channels(self) -> int: ...

        @property
        def rowstride(self) -> int: ...

        @property
        def width(self) -> int: ...

    props: _Props

    def add_alpha(self, substitute_color: builtins.bool, r: builtins.int, g: builtins.int, b: builtins.int) -> Pixbuf: ...

    def apply_embedded_orientation(self) -> Pixbuf: ...

    @staticmethod
    def calculate_rowstride(colorspace: Colorspace, has_alpha: builtins.bool, bits_per_sample: builtins.int, width: builtins.int, height: builtins.int) -> builtins.int: ...

    def composite(self, dest: Pixbuf, dest_x: builtins.int, dest_y: builtins.int, dest_width: builtins.int, dest_height: builtins.int, offset_x: builtins.float, offset_y: builtins.float, scale_x: builtins.float, scale_y: builtins.float, interp_type: InterpType, overall_alpha: builtins.int) -> None: ...

    def composite_color(self, dest: Pixbuf, dest_x: builtins.int, dest_y: builtins.int, dest_width: builtins.int, dest_height: builtins.int, offset_x: builtins.float, offset_y: builtins.float, scale_x: builtins.float, scale_y: builtins.float, interp_type: InterpType, overall_alpha: builtins.int, check_x: builtins.int, check_y: builtins.int, check_size: builtins.int, color1: builtins.int, color2: builtins.int) -> None: ...

    def composite_color_simple(self, dest_width: builtins.int, dest_height: builtins.int, interp_type: InterpType, overall_alpha: builtins.int, check_size: builtins.int, color1: builtins.int, color2: builtins.int) -> typing.Optional[Pixbuf]: ...

    def copy(self) -> typing.Optional[Pixbuf]: ...

    def copy_area(self, src_x: builtins.int, src_y: builtins.int, width: builtins.int, height: builtins.int, dest_pixbuf: Pixbuf, dest_x: builtins.int, dest_y: builtins.int) -> None: ...

    def copy_options(self, dest_pixbuf: Pixbuf) -> builtins.bool: ...

    def fill(self, pixel: builtins.int) -> None: ...

    def flip(self, horizontal: builtins.bool) -> typing.Optional[Pixbuf]: ...

    def get_bits_per_sample(self) -> builtins.int: ...

    def get_byte_length(self) -> builtins.int: ...

    def get_colorspace(self) -> Colorspace: ...

    @staticmethod
    def get_file_info(filename: builtins.str) -> typing.Tuple[typing.Optional[PixbufFormat], builtins.int, builtins.int]: ...

    @staticmethod
    def get_file_info_async(filename: builtins.str, cancellable: typing.Optional[Gio.Cancellable], callback: typing.Optional[Gio.AsyncReadyCallback], *user_data: typing.Optional[builtins.object]) -> None: ...

    @staticmethod
    def get_file_info_finish(async_result: Gio.AsyncResult) -> typing.Tuple[PixbufFormat, builtins.int, builtins.int]: ...

    @staticmethod
    def get_formats() -> typing.Sequence[PixbufFormat]: ...

    def get_has_alpha(self) -> builtins.bool: ...

    def get_height(self) -> builtins.int: ...

    def get_n_channels(self) -> builtins.int: ...

    def get_option(self, key: builtins.str) -> builtins.str: ...

    def get_options(self) -> typing.Mapping[builtins.str, builtins.str]: ...

    def get_pixels(self) -> builtins.bytes: ...

    def get_rowstride(self) -> builtins.int: ...

    def get_width(self) -> builtins.int: ...

    @staticmethod
    def init_modules(path: builtins.str) -> builtins.bool: ...

    @staticmethod
    def new(colorspace: Colorspace, has_alpha: builtins.bool, bits_per_sample: builtins.int, width: builtins.int, height: builtins.int, **kwargs) -> typing.Optional[Pixbuf]: ...  # type: ignore

    @staticmethod
    def new_from_bytes(data: GLib.Bytes, colorspace: Colorspace, has_alpha: builtins.bool, bits_per_sample: builtins.int, width: builtins.int, height: builtins.int, rowstride: builtins.int) -> Pixbuf: ...

    @staticmethod
    def new_from_data(data: builtins.bytes, colorspace: Colorspace, has_alpha: builtins.bool, bits_per_sample: builtins.int, width: builtins.int, height: builtins.int, rowstride: builtins.int, destroy_fn: typing.Optional[PixbufDestroyNotify], *destroy_fn_data: typing.Optional[builtins.object]) -> Pixbuf: ...

    @staticmethod
    def new_from_file(filename: builtins.str) -> Pixbuf: ...

    @staticmethod
    def new_from_file_at_scale(filename: builtins.str, width: builtins.int, height: builtins.int, preserve_aspect_ratio: builtins.bool) -> Pixbuf: ...

    @staticmethod
    def new_from_file_at_size(filename: builtins.str, width: builtins.int, height: builtins.int) -> Pixbuf: ...

    @staticmethod
    def new_from_inline(data: builtins.bytes, copy_pixels: builtins.bool) -> Pixbuf: ...

    @staticmethod
    def new_from_resource(resource_path: builtins.str) -> Pixbuf: ...

    @staticmethod
    def new_from_resource_at_scale(resource_path: builtins.str, width: builtins.int, height: builtins.int, preserve_aspect_ratio: builtins.bool) -> Pixbuf: ...

    @staticmethod
    def new_from_stream(stream: Gio.InputStream, cancellable: typing.Optional[Gio.Cancellable]) -> Pixbuf: ...

    @staticmethod
    def new_from_stream_async(stream: Gio.InputStream, cancellable: typing.Optional[Gio.Cancellable], callback: typing.Optional[Gio.AsyncReadyCallback], *user_data: typing.Optional[builtins.object]) -> None: ...

    @staticmethod
    def new_from_stream_at_scale(stream: Gio.InputStream, width: builtins.int, height: builtins.int, preserve_aspect_ratio: builtins.bool, cancellable: typing.Optional[Gio.Cancellable]) -> Pixbuf: ...

    @staticmethod
    def new_from_stream_at_scale_async(stream: Gio.InputStream, width: builtins.int, height: builtins.int, preserve_aspect_ratio: builtins.bool, cancellable: typing.Optional[Gio.Cancellable], callback: typing.Optional[Gio.AsyncReadyCallback], *user_data: typing.Optional[builtins.object]) -> None: ...

    @staticmethod
    def new_from_stream_finish(async_result: Gio.AsyncResult) -> Pixbuf: ...

    @staticmethod
    def new_from_xpm_data(data: typing.Sequence[builtins.str]) -> Pixbuf: ...

    def new_subpixbuf(self, src_x: builtins.int, src_y: builtins.int, width: builtins.int, height: builtins.int) -> Pixbuf: ...

    def read_pixel_bytes(self) -> GLib.Bytes: ...

    def read_pixels(self) -> builtins.int: ...

    def remove_option(self, key: builtins.str) -> builtins.bool: ...

    def rotate_simple(self, angle: PixbufRotation) -> typing.Optional[Pixbuf]: ...

    def saturate_and_pixelate(self, dest: Pixbuf, saturation: builtins.float, pixelate: builtins.bool) -> None: ...

    def save_to_bufferv(self, type: builtins.str, option_keys: typing.Sequence[builtins.str], option_values: typing.Sequence[builtins.str]) -> typing.Tuple[builtins.bool, builtins.bytes]: ...

    def save_to_callbackv(self, save_func: PixbufSaveFunc, user_data: typing.Optional[builtins.object], type: builtins.str, option_keys: typing.Sequence[builtins.str], option_values: typing.Sequence[builtins.str]) -> builtins.bool: ...

    @staticmethod
    def save_to_stream_finish(async_result: Gio.AsyncResult) -> builtins.bool: ...

    def save_to_streamv(self, stream: Gio.OutputStream, type: builtins.str, option_keys: typing.Sequence[builtins.str], option_values: typing.Sequence[builtins.str], cancellable: typing.Optional[Gio.Cancellable]) -> builtins.bool: ...

    def save_to_streamv_async(self, stream: Gio.OutputStream, type: builtins.str, option_keys: typing.Sequence[builtins.str], option_values: typing.Sequence[builtins.str], cancellable: typing.Optional[Gio.Cancellable], callback: typing.Optional[Gio.AsyncReadyCallback], *user_data: typing.Optional[builtins.object]) -> None: ...

    def savev(self, filename: builtins.str, type: builtins.str, option_keys: typing.Sequence[builtins.str], option_values: typing.Sequence[builtins.str]) -> builtins.bool: ...

    def scale(self, dest: Pixbuf, dest_x: builtins.int, dest_y: builtins.int, dest_width: builtins.int, dest_height: builtins.int, offset_x: builtins.float, offset_y: builtins.float, scale_x: builtins.float, scale_y: builtins.float, interp_type: InterpType) -> None: ...

    def scale_simple(self, dest_width: builtins.int, dest_height: builtins.int, interp_type: InterpType) -> typing.Optional[Pixbuf]: ...

    def set_option(self, key: builtins.str, value: builtins.str) -> builtins.bool: ...


class PixbufAnimation(GObject.Object):

    def get_height(self) -> builtins.int: ...

    def get_iter(self, start_time: typing.Optional[GLib.TimeVal]) -> PixbufAnimationIter: ...

    def get_static_image(self) -> Pixbuf: ...

    def get_width(self) -> builtins.int: ...

    def is_static_image(self) -> builtins.bool: ...

    @staticmethod
    def new_from_file(filename: builtins.str) -> PixbufAnimation: ...

    @staticmethod
    def new_from_resource(resource_path: builtins.str) -> PixbufAnimation: ...

    @staticmethod
    def new_from_stream(stream: Gio.InputStream, cancellable: typing.Optional[Gio.Cancellable]) -> PixbufAnimation: ...

    @staticmethod
    def new_from_stream_async(stream: Gio.InputStream, cancellable: typing.Optional[Gio.Cancellable], callback: typing.Optional[Gio.AsyncReadyCallback], *user_data: typing.Optional[builtins.object]) -> None: ...

    @staticmethod
    def new_from_stream_finish(async_result: Gio.AsyncResult) -> PixbufAnimation: ...


class PixbufAnimationIter(GObject.Object):

    def advance(self, current_time: typing.Optional[GLib.TimeVal]) -> builtins.bool: ...

    def get_delay_time(self) -> builtins.int: ...

    def get_pixbuf(self) -> Pixbuf: ...

    def on_currently_loading_frame(self) -> builtins.bool: ...


class PixbufLoader(GObject.Object):
    parent_instance: GObject.Object
    priv: builtins.object

    def close(self) -> builtins.bool: ...

    def get_animation(self) -> PixbufAnimation: ...

    def get_format(self) -> typing.Optional[PixbufFormat]: ...

    def get_pixbuf(self) -> Pixbuf: ...

    @staticmethod
    def new(**kwargs) -> PixbufLoader: ...  # type: ignore

    @staticmethod
    def new_with_mime_type(mime_type: builtins.str) -> PixbufLoader: ...

    @staticmethod
    def new_with_type(image_type: builtins.str) -> PixbufLoader: ...

    def set_size(self, width: builtins.int, height: builtins.int) -> None: ...

    def write(self, buf: builtins.bytes) -> builtins.bool: ...

    def write_bytes(self, buffer: GLib.Bytes) -> builtins.bool: ...

    def do_area_prepared(self) -> None: ...

    def do_area_updated(self, x: builtins.int, y: builtins.int, width: builtins.int, height: builtins.int) -> None: ...

    def do_closed(self) -> None: ...

    def do_size_prepared(self, width: builtins.int, height: builtins.int) -> None: ...


class PixbufSimpleAnim(PixbufAnimation):

    def add_frame(self, pixbuf: Pixbuf) -> None: ...

    def get_loop(self) -> builtins.bool: ...

    @staticmethod
    def new(width: builtins.int, height: builtins.int, rate: builtins.float) -> PixbufSimpleAnim: ...

    def set_loop(self, loop: builtins.bool) -> None: ...


class PixbufSimpleAnimIter(PixbufAnimationIter):
    ...


class PixbufFormat():

    def copy(self) -> PixbufFormat: ...

    def free(self) -> None: ...

    def get_description(self) -> builtins.str: ...

    def get_extensions(self) -> typing.Sequence[builtins.str]: ...

    def get_license(self) -> builtins.str: ...

    def get_mime_types(self) -> typing.Sequence[builtins.str]: ...

    def get_name(self) -> builtins.str: ...

    def is_disabled(self) -> builtins.bool: ...

    def is_save_option_supported(self, option_key: builtins.str) -> builtins.bool: ...

    def is_scalable(self) -> builtins.bool: ...

    def is_writable(self) -> builtins.bool: ...

    def set_disabled(self, disabled: builtins.bool) -> None: ...


class Colorspace(GObject.GEnum, builtins.int):
    RGB = ...  # type: Colorspace


class InterpType(GObject.GEnum, builtins.int):
    BILINEAR = ...  # type: InterpType
    HYPER = ...  # type: InterpType
    NEAREST = ...  # type: InterpType
    TILES = ...  # type: InterpType


class PixbufAlphaMode(GObject.GEnum, builtins.int):
    BILEVEL = ...  # type: PixbufAlphaMode
    FULL = ...  # type: PixbufAlphaMode


class PixbufError(GObject.GEnum, builtins.int):
    BAD_OPTION = ...  # type: PixbufError
    CORRUPT_IMAGE = ...  # type: PixbufError
    FAILED = ...  # type: PixbufError
    INCOMPLETE_ANIMATION = ...  # type: PixbufError
    INSUFFICIENT_MEMORY = ...  # type: PixbufError
    UNKNOWN_TYPE = ...  # type: PixbufError
    UNSUPPORTED_OPERATION = ...  # type: PixbufError

    @staticmethod
    def quark() -> builtins.int: ...


class PixbufRotation(GObject.GEnum, builtins.int):
    CLOCKWISE = ...  # type: PixbufRotation
    COUNTERCLOCKWISE = ...  # type: PixbufRotation
    NONE = ...  # type: PixbufRotation
    UPSIDEDOWN = ...  # type: PixbufRotation


PixbufDestroyNotify = typing.Callable[[builtins.bytes, typing.Optional[builtins.object]], None]
PixbufSaveFunc = typing.Callable[[builtins.bytes, typing.Optional[builtins.object]], typing.Tuple[builtins.bool, GLib.Error]]


def pixbuf_error_quark() -> builtins.int: ...


PIXBUF_FEATURES_H: builtins.int
PIXBUF_MAJOR: builtins.int
PIXBUF_MICRO: builtins.int
PIXBUF_MINOR: builtins.int
PIXBUF_VERSION: builtins.str
