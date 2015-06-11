package test;

import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import com.google.common.collect.Lists;
import com.google.common.collect.Maps;

/**
 * 给MM写的计算婚姻的算法
 * 
 * @author <a href="mailto:wangyuxuan@dangdang.com">Yuxuan Wang</a>
 *
 */
public class Matches {

	public static void main(String[] args) {
		// 数据初始化
		Map<String, List<String>> males = Maps.newLinkedHashMap();
		males.put("Xavier", Lists.newArrayList("Amy", "Bertha", "Clare"));
		males.put("Zeus", Lists.newArrayList("Amy", "Bertha", "Clare"));
		males.put("Yancey", Lists.newArrayList("Bertha", "Amy", "Clare"));

		Map<String, List<String>> females = Maps.newLinkedHashMap();
		females.put("Amy", Lists.newArrayList("Yancey", "Xavier", "Zeus"));
		females.put("Bertha", Lists.newArrayList("Xavier", "Yancey", "Zeus"));
		females.put("Clare", Lists.newArrayList("Xavier", "Yancey", "Zeus"));

		// 配对结果
		Map<String, String> mm = Maps.newLinkedHashMap();
		Map<String, String> fm = Maps.newLinkedHashMap();

		// 各种前任
		Map<String, List<String>> rejects = Maps.newHashMap();

		int couples = 0;
		// 如果未全部配对
		while (couples < 3) {
			for (Entry<String, List<String>> entry : males.entrySet()) {
				String male = entry.getKey();
				// 如果已经找到girl了，让给他人吧
				if (mm.containsKey(male)) {
					continue;
				}
				// 依次循环我喜欢的girls
				for (String female : entry.getValue()) {
					// 如果这个girl以前没有和我dating过
					if (!rejects.containsKey(male) || !rejects.get(male).contains(female)) {
						String curr = fm.get(female);
						List<String> list = females.get(female);
						if (curr == null) {
							// 如果这个girl没人约，让我来吧！
							mm.put(male, female);
							fm.put(female, male);
							couples++;
							break;
						} else if (list.indexOf(male) < list.indexOf(curr)) {
							// 如果这个girl有人约了，但是她更喜欢我，就让她甩了前任，跟我吧！
							mm.remove(curr);
							if (!rejects.containsKey(curr)) {
								rejects.put(curr, Lists.<String> newArrayList());
							}
							rejects.get(curr).add(female);
							mm.put(male, female);
							fm.put(female, male);
							break;
						}
					}
				}
			}
		}

		// 打印结果
		System.out.println(mm);
		System.out.println(fm);

	}

}
