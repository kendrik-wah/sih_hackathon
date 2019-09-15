import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.util.ArrayList;
import java.io.IOException;

public class jsoup_test {

	private static ArrayList <String> urls = new ArrayList<String>();

	public static void main(String[] args) throws IOException {
		Document doc = Jsoup.connect("https://www.reddit.com/live/133sixros7tu5/").get();
		Elements elems = doc.select("ol.liveupdate-listing");
		for (Element elem: elems.select("a[href]")) {
			String url = elem.attr("href");
			if (url.contains("https")) {
				urls.add(url);
				System.out.println(url);
			}
		}
	}
}