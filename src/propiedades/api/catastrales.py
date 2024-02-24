from flask import Response, redirect, render_template, request, session, url_for

import propiedades.seedwork.presentation.api as api


bp = api.crear_blueprint("catastral", "/catastrales")
