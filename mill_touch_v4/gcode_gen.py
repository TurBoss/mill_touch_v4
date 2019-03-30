# Smart G code thingy
import linuxcnc

def preambleAdd(parent):
    parent.gcodeListWidget.addItem("; G code generated by the JT's G code wizard")
    parent.gcodeListWidget.addItem(parent.gcodePreambleLine.text())

def gcodeAppend(parent):
    if parent.spotEnableBtn.isChecked():
        parent.gcodeListWidget.addItem('; Spot Op')
        if parent.spotRpmLbl.text():
            parent.gcodeListWidget.addItem('M3 S{}'.format(parent.spotRpmLbl.text()))
        if parent.spotFeedLbl.text():
            parent.gcodeListWidget.addItem('F{}'.format(parent.spotFeedLbl.text()))
        if parent.coordListWidget.count() > 0: # toss out an error if not
            for i in range(parent.coordListWidget.count()):
                coordinates = parent.coordListWidget.item(i).text()
                zDepth = parent.spotDepthLbl.text()
                zClear = parent.spotRetractLbl.text()
                if i == 0:
                    parent.gcodeListWidget.addItem('G81 {} Z{} R{}'.format(coordinates, zDepth, zClear))
                else:
                    parent.gcodeListWidget.addItem('{}'.format(coordinates))

    if parent.drillEnableBtn.isChecked():
        parent.gcodeListWidget.addItem('; Drill Op')
        if parent.drillRpmLbl.text():
            parent.gcodeListWidget.addItem('M3 S{}'.format(parent.drillRpmLbl.text()))
        if parent.drillFeedLbl.text():
            parent.gcodeListWidget.addItem('F{}'.format(parent.drillFeedLbl.text()))
        if parent.coordListWidget.count() > 0: # toss out an error if not
            for i in range(parent.coordListWidget.count()):
                coordinates = parent.coordListWidget.item(i).text()
                zDepth = parent.drillDepthLbl.text()
                zClear = parent.drillRetractLbl.text()
                if i == 0:
                    parent.gcodeListWidget.addItem('G81 {} Z{} R{}'.format(coordinates, zDepth, zClear))
                else:
                    parent.gcodeListWidget.addItem('{}'.format(coordinates))

    if parent.reamEnableBtn.isChecked():
        parent.gcodeListWidget.addItem('; Ream Op')
        if parent.reamRpmLbl.text():
            parent.gcodeListWidget.addItem('M3 S{}'.format(parent.reamRpmLbl.text()))
        if parent.reamFeedLbl.text():
            parent.gcodeListWidget.addItem('F{}'.format(parent.reamFeedLbl.text()))
        if parent.coordListWidget.count() > 0: # toss out an error if not
            for i in range(parent.coordListWidget.count()):
                coordinates = parent.coordListWidget.item(i).text()
                zDepth = parent.reamZdepthLbl.text()
                zClear = parent.reamRetractLbl.text()
                if i == 0:
                    parent.gcodeListWidget.addItem('G81 {} Z{} R{}'.format(coordinates, zDepth, zClear))
                else:
                    parent.gcodeListWidget.addItem('{}'.format(coordinates))

    if parent.chamferEnableBtn.isChecked():
        parent.gcodeListWidget.addItem('; Ream Op')
        if parent.reamRpmLbl.text():
            parent.gcodeListWidget.addItem('M3 S{}'.format(parent.reamRpmLbl.text()))
        if parent.reamFeedLbl.text():
            parent.gcodeListWidget.addItem('F{}'.format(parent.reamFeedLbl.text()))
        if parent.coordListWidget.count() > 0: # toss out an error if not
            for i in range(parent.coordListWidget.count()):
                coordinates = parent.coordListWidget.item(i).text()
                zDepth = parent.reamZdepthLbl.text()
                zClear = parent.reamRetractLbl.text()
                if i == 0:
                    parent.gcodeListWidget.addItem('G81 {} Z{} R{}'.format(coordinates, zDepth, zClear))
                else:
                    parent.gcodeListWidget.addItem('{}'.format(coordinates))


def postambleAppend(parent):
    parent.gcodeListWidget.addItem('M2')

def gcodeLoad(parent):
    emcCommand = linuxcnc.command()
    gcode = []
    with open('/tmp/qtpyvcp.ngc','w') as f:
        for i in range(parent.gcodeListWidget.count()):
            gcode.append(parent.gcodeListWidget.item(i).text())
        f.write('\n'.join(gcode))
    emcCommand.reset_interpreter()
    emcCommand.program_open('/tmp/qtpyvcp.ngc')

def clearGcode(parent):
    parent.gcodeListWidget.clear()

def reloadProgram(parent):
    emcStat = linuxcnc.stat()
    emcStat.poll()
    origGcodeFile = emcStat.file
    print(origGcodeFile)
    with open('/tmp/temp.ngc','w') as f:
        f.write('%\n%')
    emcCommand = linuxcnc.command()
    emcCommand.program_open('/tmp/temp.ngc')
    emcCommand.wait_complete()
    emcStat.poll()
    gcodeFile = emcStat.file
    print(gcodeFile)
    emcCommand.program_open(origGcodeFile)
    emcCommand.wait_complete()
    emcStat.poll()
    gcodeFile = emcStat.file
    print(gcodeFile)



