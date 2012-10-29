/**
 * Load embed XML file data.
 * this sample load XML file's content like this.
 * -- mst_sex.xml --
 * <?xml version="1.0" encoding="UTF-8" ?>
 * <mst_sex>
 *   <sex>
 *     <code>M</code>
 *     <name>Male</name>
 *   </sex>
 *   <sex>
 *     <code>F</code>
 *     <name>Female</name>
 *   </sex>
 * </mst_sex>
 * -- mst_sex.xml --
 * mst_sex.xml arranged at [project]/src/master_datas/mst_sex.xml
 */

import mx.core.ByteArrayAsset;

/**
 * load sample class..
 */
public class Test {
	/**  */
	[Embed(source="master_datas/mst_sex.xml", mimeType="application/octet-stream")]
	private static const CLS_MST_SEX:Class;
	
	/**
	 *
	 */
	private function loadXML():void {
		var byteaset:ByteArrayAsset = ByteArrayAsset(new CLS_MST_SEX());
		var xmlstring:String = byteaset.readUTFBytes(byteaset.length);
		var mstSex:XML = new XML(xmlstring);
		trace("test start");
		trace("sex len:" + mstSex.sex.length());
		trace("sex 0:" + mstSex.sex[0]);
		trace("  code:" + mstSex.sex[0].code);
		trace("  name:" + mstSex.sex[0].name);
		trace("sex 1:" + mstSex.sex[1]);
		trace("  code:" + mstSex.sex[1].code);
		trace("  name:" + mstSex.sex[1].name);
		trace("test end");
	}
}

