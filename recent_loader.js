// recent_loader.js — lista proyectos recientes de Ableton y pide abrirlos.
// inlets:  0 bang (recarga), 1 int (seleccion), 2 bang (abrir)
// outlets: 0 -> umenu (clear / append ...)
autowatch = 1;
inlets = 3;
outlets = 1;

var JSON_PATH = "/Users/jorgenavaslosada/Documents/AbletonRecent/recent.json";
var REQ_PATH = "/Users/jorgenavaslosada/Documents/AbletonRecent/request.txt";
var items = [];
var sel = -1;

function readAllText(path) {
    var f = new File(path);          // abre en modo lectura
    var txt = "";
    if (f.isopen) {
        var line;
        while ((line = f.readline()) != null) {
            txt += line + "\n";
        }
        f.close();
    }
    return txt;
}

function loadData() {
    items = [];
    sel = -1;
    try {
        var txt = readAllText(JSON_PATH);
        if (txt == "") {
            post("recent_loader: no pude abrir " + JSON_PATH + "\n");
            return;
        }
        items = JSON.parse(txt);
        post("recent_loader: " + items.length + " proyectos\n");
        outlet(0, "clear");
        for (var i = 0; i < items.length; i++) {
            outlet(0, "append", items[i].name);
        }
    } catch (e) {
        post("recent_loader ERROR loadData: " + e + "\n");
    }
}

function msg_int(v) {
    if (this.inlet === 1) {
        sel = v;
    }
}

function bang() {
    if (this.inlet === 0) {
        loadData();
    } else if (this.inlet === 2) {
        openSelected();
    }
}

function openSelected() {
    try {
        if (sel < 0 || sel >= items.length) {
            post("recent_loader: selecciona un proyecto de la lista\n");
            return;
        }
        var f = new File(REQ_PATH, "write", "TEXT");
        if (f.isopen) {
            f.position = 0;
            f.writestring(JSON.stringify(items[sel]));
            f.eof = f.position;
            f.close();
            post("recent_loader: pedido abrir -> " + items[sel].path + "\n");
        } else {
            post("recent_loader: no pude escribir " + REQ_PATH + "\n");
        }
    } catch (e) {
        post("recent_loader ERROR openSelected: " + e + "\n");
    }
}

function loadbang() {
    loadData();
}
