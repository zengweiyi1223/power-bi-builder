from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import argparse


ROOT = Path(__file__).parent / "images-v3"
ROOT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1440

BG = "#F4F6FB"
PAPER = "#FFFFFF"
INK = "#182238"
MUTED = "#66728A"
BLUE = "#4B66E8"
BLUE_D = "#344FBF"
BLUE_L = "#E7ECFF"
TEAL = "#218B82"
TEAL_L = "#E3F3F0"
AMBER = "#D99B2B"
AMBER_L = "#FFF2D2"
RED = "#D75A70"
RED_L = "#FBEAED"
LINE = "#D9E0EC"
FLOW_LINE = "#BCC9DD"
BODY = "#52617A"
SOFT = "#EBF0F8"
FONT_REG = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"


def ft(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def tw(draw, text, f):
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0]


def wrapped(draw, text, f, width):
    result = []
    for para in text.split("\n"):
        if not para:
            result.append("")
            continue
        line = ""
        for char in para:
            candidate = line + char
            if line and tw(draw, candidate, f) > width:
                result.append(line)
                line = char
            else:
                line = candidate
        result.append(line)
    return result


def put(draw, x, y, text, size=22, color=INK, bold=False, width=None, gap=7, align="left"):
    f = ft(size, bold)
    if width is None:
        draw.text((x, y), text, font=f, fill=color)
        return size + gap
    lines = wrapped(draw, text, f, width)
    for line in lines:
        offset = width - tw(draw, line, f)
        xx = x + (offset / 2 if align == "center" else offset if align == "right" else 0)
        draw.text((xx, y), line, font=f, fill=color)
        y += size + gap
    return len(lines) * (size + gap)


def rr(draw, xy, fill=PAPER, outline=None, radius=18, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width if outline else 1)


def line(draw, points, color=LINE, width=3):
    draw.line(points, fill=color, width=width, joint="curve")


def arrow(draw, start, end, color=BLUE, width=4, size=13):
    draw.line((start, end), fill=color, width=width)
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    p1 = (end[0]-size*math.cos(angle-.52), end[1]-size*math.sin(angle-.52))
    p2 = (end[0]-size*math.cos(angle+.52), end[1]-size*math.sin(angle+.52))
    draw.polygon((end, p1, p2), fill=color)


def dot(draw, x, y, color=BLUE, r=7):
    draw.ellipse((x-r, y-r, x+r, y+r), fill=color)


def badge(draw, x, y, text, color=BLUE, bg=BLUE_L, size=19, px=14, py=7):
    f = ft(size, True)
    w = tw(draw, text, f) + px*2
    h = size + py*2 + 2
    rr(draw, (x, y, x+w, y+h), bg, radius=h//2)
    draw.text((x+px, y+py-1), text, font=f, fill=color)
    return w


def header_footer(page, title, summary, next_line, right_header=False, title_size=45):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((58, 34), "AI-native workflow", font=ft(24, True), fill=BLUE_D)
    d.text((58, 67), "人与 AI 协作 · 项目闭环", font=ft(17), fill=MUTED)
    header = f"{page:02d} / 06  •  山楂条"
    d.text((1022-tw(d, header, ft(20, True)), 39), header, font=ft(20, True), fill=MUTED)
    line(d, ((58, 105), (1022, 105)), LINE, 2)
    put(d, 58, 131, title, size=title_size, bold=True, width=958, gap=2)
    line(d, ((58, 1334), (1022, 1334)), LINE, 2)
    d.text((58, 1350), "本页总结", font=ft(16, True), fill=BLUE_D)
    put(d, 154, 1347, summary, size=18, bold=True, width=868, gap=1)
    closing = "后续  " + next_line if page == 6 else "下一页  " + next_line + "  →"
    put(d, 58, 1390, closing, size=17, color=MUTED)
    return im, d


def section(d, x, y, title, color=BLUE):
    d.text((x, y), title, font=ft(25, True), fill=color)


def small_flow_node(d, cx, cy, title, detail=None, color=BLUE, width=150, title_size=19):
    d.ellipse((cx-13, cy-13, cx+13, cy+13), fill=color)
    put(d, cx-width//2, cy+25, title, title_size, INK, True, width, 4, "center")
    if detail:
        put(d, cx-width//2, cy+56, detail, 15, MUTED, False, width, 3, "center")


def page1(style="plain"):
    im, d = header_footer(1, "AI 会写代码，\n项目为什么还是容易卡住？",
                          "卡点常出在需求、验收、记录和恢复，不只是代码。",
                          "传统岗位流程与人机协作流程的差别", right_header=True, title_size=49)
    badge(d, 58, 263, "常见卡点 · 按项目阶段看", BLUE_D, BLUE_L, 21)
    groups = [
        ("项目开始前", BLUE, [
            ("目标不清", "目标和成功标准说不具体。"),
            ("范围漂移", "做什么、不做什么没定，需求越聊越多。"),
            ("方向未对齐", "人和 AI 对目标、方案或验收理解不同。"),
            ("准备不足", "输入、环境、权限和回退条件没有核实。"),
        ]),
        ("项目进行中", TEAL, [
            ("任务难拆", "先后依赖不清，风险和难度没排出来。"),
            ("执行会跑偏", "AI 可能误解业务，或越过已定边界。"),
            ("验证太晚", "做了很多才发现结果不对或场景没覆盖。"),
            ("失败难归因", "业务、代码、依赖和环境问题混在一起。"),
        ]),
        ("项目结束后", AMBER, [
            ("缺少验收证据", "声称完成，却缺少可复核的验收证据。"),
            ("状态不清", "把已构建、已发布和已可用当成一回事。"),
            ("交接断层", "决策、限制、运行方式和未完成项找不到。"),
            ("出了问题难恢复", "没有清晰检查点，不知道如何继续或回退。"),
        ]),
    ]
    top_positions = [326, 585, 844]
    for (phase, color, items), top in zip(groups, top_positions):
        tint = {BLUE: "#E7ECFF", TEAL: "#E3F3F0", AMBER: "#FFF2D2"}[color]
        item_top = top + 52
        if style == "outline":
            rr(d, (58, top-6, 1022, top+231), PAPER, color, 18, 3)
            badge(d, 82, top+7, phase, PAPER, color, size=21, px=14, py=6)
            item_top = top + 58
        elif style == "tint":
            rr(d, (58, top-6, 1022, top+231), tint, radius=18)
            d.text((82, top+4), phase, font=ft(27, True), fill=color)
            line(d, ((82, top+43), (1000, top+43)), color, 2)
            item_top = top + 58
        elif style == "rail":
            rr(d, (58, top-6, 1022, top+231), PAPER, LINE, 18, 2)
            rr(d, (58, top-6, 75, top+231), color, radius=8)
            rr(d, (91, top+3, 105, top+34), color, radius=6)
            d.text((122, top), phase, font=ft(27, True), fill=color)
            item_top = top + 54
        else:
            d.text((58, top), phase, font=ft(27, True), fill=color)
        for idx, (issue, detail) in enumerate(items):
            col, row = idx % 2, idx // 2
            x = 82 + col*472
            y = item_top + row*82
            d.ellipse((x, y+9, x+12, y+21), fill=color)
            d.text((x+22, y), issue, font=ft(24, True), fill=INK)
            put(d, x+22, y+34, detail, 21, MUTED, False, 415, 3)
        if style == "plain" and top != top_positions[-1]:
            line(d, ((82, top+236), (1022, top+236)), LINE, 2)
    rr(d, (58, 1110, 1022, 1244), fill="#E9EEF8", radius=20)
    put(d, 84, 1133, "理想状态：目标清楚、每步可验证、问题能定位、结果可恢复，下一轮也接得上。", 24, INK, True, 900, 7)
    return im


def page2():
    im, d = header_footer(2, "开发目标不变，协作分工变了",
                          "两种流程目标一致；变化的是岗位职责如何组合与协作。",
                          "不同项目，流程要怎么裁剪", title_size=49)
    badge(d, 58, 263, "共同目标 · 职责重新组合", BLUE_D, BLUE_L, size=21)

    put(d, 58, 318, "传统开发｜典型岗位流程", 30, INK, True, 960, 4)
    put(d, 58, 358, "岗位各有侧重，开发与测试反复验证；发布反馈带来下一轮改进。", 20, MUTED, False, 960, 4)
    traditional = [
        ("产品 / 业务", "目标与需求"),
        ("UI / UX", "交互与体验"),
        ("技术方案", "架构与选型"),
        ("开发与测试", "实现与验证"),
        ("发布 / 运维", "上线与监控"),
    ]
    card_w, card_h, card_y = 176, 126, 403
    card_xs = [58, 254, 450, 646, 842]
    flow_color = BLUE_D
    for i, ((title, detail), x) in enumerate(zip(traditional, card_xs)):
        rr(d, (x, card_y, x+card_w, card_y+card_h), PAPER, FLOW_LINE, 15, 3)
        put(d, x+10, card_y+23, title, 24, INK, True, card_w-20, 4, "center")
        put(d, x+10, card_y+68, detail, 22, BODY, False, card_w-20, 4, "center")
        if i < len(traditional)-1:
            arrow(d, (x+card_w+2, card_y+card_h//2), (card_xs[i+1]-3, card_y+card_h//2), flow_color, 3, 9)

    # Operations feed the next iteration: a return path, not a one-way handoff.
    last_cx, first_cx = card_xs[-1]+card_w//2, card_xs[0]+card_w//2
    line(d, ((last_cx, card_y+card_h), (last_cx, 562), (first_cx, 562)), flow_color, 3)
    arrow(d, (first_cx, 562), (first_cx, card_y+card_h+2), flow_color, 3, 9)
    d.text((379, 569), "运行反馈回到需求与方案", font=ft(19, True), fill=BLUE_D)

    line(d, ((58, 606), (1022, 606)), LINE, 2)
    put(d, 58, 631, "人与 AI 协作｜通用流程", 30, INK, True, 960, 4)
    put(d, 58, 671, "人负责判断与授权；AI 在明确边界内协助执行。", 20, MUTED, False, 960, 4)
    collaboration = [
        ("目标与边界", "人主责：明确目标\n与验收标准"),
        ("需求与方案", "人判断取舍\nAI 协助分析"),
        ("实现与验证", "AI 实现与自检\n独立验证与复核"),
        ("交付与运行", "人验收并批准\n明确后续维护责任"),
    ]
    lower_w, lower_h, lower_y = 220, 145, 719
    lower_xs = [58, 306, 554, 802]
    for i, ((title, detail), x) in enumerate(zip(collaboration, lower_xs)):
        rr(d, (x, lower_y, x+lower_w, lower_y+lower_h), PAPER, FLOW_LINE, 15, 3)
        put(d, x+12, lower_y+27, title, 24, INK, True, lower_w-24, 4, "center")
        put(d, x+12, lower_y+72, detail, 22, BODY, False, lower_w-24, 5, "center")
        if i < len(collaboration)-1:
            arrow(d, (x+lower_w+3, lower_y+lower_h//2), (lower_xs[i+1]-4, lower_y+lower_h//2), TEAL, 3, 9)

    # Human review and delivery feedback return to the next planning cycle.
    line(d, ((lower_xs[-1]+lower_w//2, lower_y+lower_h), (lower_xs[-1]+lower_w//2, 909), (lower_xs[0]+lower_w//2, 909)), TEAL, 3)
    arrow(d, (lower_xs[0]+lower_w//2, 909), (lower_xs[0]+lower_w//2, lower_y+lower_h+2), TEAL, 3, 9)
    d.text((379, 917), "验收与运行结果，反馈到下一轮", font=ft(19, True), fill=TEAL)

    rr(d, (58, 975, 1022, 1278), "#E9EEF8", radius=20)
    d.text((84, 1003), "岗位不是逐个被替换，而是按优势重新组合", font=ft(25, True), fill=BLUE_D)
    put(d, 84, 1058, "人：明确目标、业务取舍、风险授权，并对验收与发布负责。", 22, INK, False, 890, 8)
    put(d, 84, 1117, "AI：在约定范围内协助分析、起草方案、实现功能和重复检查。", 22, INK, False, 890, 8)
    put(d, 84, 1180, "阶段内实现—验证反复进行；必要时人工复核。谁执行、谁确认，随项目风险调整。", 20, MUTED, True, 890, 5)
    return im


def page3():
    im, d = header_footer(3, "不同项目，流程如何裁剪？",
                          "所有项目共享目标、契约、验证和交接；具体阶段与控制随风险裁剪。",
                          "看人、AI、文档与 Git 怎样互相补位")
    badge(d, 58, 263, "同一骨架 · 控制随风险裁剪", BLUE_D, BLUE_L, size=21)
    put(d, 58, 318, "常见项目类型｜重点因项目而异", 30, INK, True, 960, 4)
    types = [
        ("实验与原型", "核心假设、成功判据", "新技术验证、概念样机"),
        ("文档与内容", "受众、内容准确性", "知识库、操作指南"),
        ("数据分析", "指标口径、数据验证", "销售趋势、经营看板"),
        ("组件与自动化", "接口、边界与恢复", "数据校验组件、定时对账"),
        ("交互应用", "交互体验、状态处理", "库存查询、预约工具"),
        ("生产服务", "权限、发布与运维", "指标 API、在线业务服务"),
    ]
    table_top, header_h, row_h = 368, 44, 43
    def cell(x, cy, text, size=22, bold=False, color=BODY, width=0):
        f = ft(size, bold)
        box = d.textbbox((0, 0), text, font=f)
        d.text((x+(width-tw(d, text, f))/2, cy-(box[1]+box[3])/2), text, font=f, fill=color)
    columns = [(58, 226), (284, 324), (608, 414)]
    for (x, width), label in zip(columns, ("类型", "重点环节", "例子")):
        cell(x, table_top+header_h/2, label, 23, True, BLUE_D, width)
    line(d, ((58, table_top+header_h), (1022, table_top+header_h)), FLOW_LINE, 2)
    for i, (kind, focus, examples) in enumerate(types):
        yy = table_top + header_h + i*row_h
        if i:
            line(d, ((58, yy), (1022, yy)), LINE, 1)
        for (x, width), text, bold, color in zip(columns, (kind, focus, examples), (True, False, False), (INK, BODY, BODY)):
            cell(x, yy+row_h/2, text, 22, bold, color, width)

    put(d, 58, 696, "两个数据项目｜按风险裁剪流程", 30, INK, True, 960, 4)
    case_y, case_h, case_w = 748, 550, 456
    cases = [
        {
            "x": 58, "tag": "案例 A｜低风险 · 本地运行", "tag_color": BLUE_D, "tag_bg": BLUE_L,
            "title": "CSV 质量检查器", "scope": "单机使用 · 虚构样例 · 不发布",
            "steps": [
                ("冻结输入与规则", "固定样例：空值、完全重复行"),
                ("实现并对照样例", "核对问题行与汇总，不扩需求"),
                ("本地交付", "给出运行说明，暂不部署"),
            ],
        },
        {
            "x": 566, "tag": "案例 B｜多人使用 · 更多控制", "tag_color": AMBER, "tag_bg": AMBER_L,
            "title": "部门共享销售看板", "scope": "多人共享 · 业务数据 · 需要权限控制",
            "steps": [
                ("先定数据边界", "确认指标、可见范围与脱敏"),
                ("分任务实现", "数据、看板、权限分步实现"),
                ("复核后修正", "核对指标、权限与异常数据"),
                ("人工批准后发布", "先备恢复措施，上线后监控"),
            ],
        },
    ]
    # Equal node widths follow the longest label across both examples.
    node_w = math.ceil(max(max(tw(d, stage, ft(24)), tw(d, detail, ft(21)))
                          for case in cases for stage, detail in case["steps"])) + 32
    for case in cases:
        x = case["x"]
        rr(d, (x, case_y, x+case_w, case_y+case_h), PAPER, FLOW_LINE, 20, 3)
        badge_w = tw(d, case["tag"], ft(20, True))+22
        badge(d, x+(case_w-badge_w)/2, case_y+18, case["tag"], case["tag_color"], case["tag_bg"], size=20, px=11, py=6)
        put(d, x+22, case_y+63, case["title"], 27, INK, True, case_w-44, 4, "center")
        put(d, x+22, case_y+103, case["scope"], 21, MUTED, False, case_w-44, 4, "center")
        step_count = len(case["steps"])
        step_gap = 126 if step_count == 3 else 96
        step_start = case_y + (175 if step_count == 3 else 155)
        for i, (stage, detail) in enumerate(case["steps"]):
            sy = step_start + i*step_gap
            node_h = 74
            nx = x + (case_w-node_w)/2
            border = "#B8C7F4" if case["tag_color"] == BLUE_D else "#E4CB8F"
            rr(d, (nx, sy, nx+node_w, sy+node_h), PAPER, border, 13, 3)
            put(d, nx+16, sy+5, stage, 24, INK, False, node_w-32, 2, "center")
            put(d, nx+16, sy+38, detail, 21, BODY, False, node_w-32, 2, "center")
            if i < step_count-1:
                arrow(d, (x+case_w//2, sy+node_h+2), (x+case_w//2, sy+step_gap-2), case["tag_color"], 2, 7)

    # The footer carries the summary; give the examples this space instead.
    return im


def page4():
    im, d = header_footer(4, "不止人与 AI，文档和 Git 也要参与",
                          "人定目标与授权，AI 按范围协助；文档留约定，Git 留改动与恢复点。",
                          "把经验变成真正能执行的注意事项")
    badge(d, 58, 263, "四种角色 · 各有长处与边界", BLUE_D, BLUE_L, size=21)
    put(d, 58, 318, "人和 AI 协作；文档记约定与证据，Git 记变更与恢复点。", 21, MUTED, True, 960, 4)

    roles = [
        ("人", "明确目标与业务事实；\n审核内容、决定取舍。", "会忙、会忘；隐含假设\n可能没有表达清楚。", BLUE, BLUE_L, 58, 370),
        ("AI", "分析、起草与实现；\n按授权更新、报告异常。", "可能误解、出错；不能\n自证成功或替人担责。", TEAL, TEAL_L, 622, 370),
        ("文档", "保存契约、决策、证据\n与交接；AI 协助维护。", "会过期或重复；须确认\n当前有效版本。", AMBER, AMBER_L, 58, 918),
        ("Git", "记录差异与版本；\n建立检查点、支持恢复。", "能恢复文件状态；业务\n结果仍需独立验收。", RED, RED_L, 622, 918),
    ]
    card_w, card_h = 400, 300
    for name, duty, limit, color, tint, x, y in roles:
        rr(d, (x, y, x+card_w, y+card_h), PAPER, FLOW_LINE, 20, 3)
        badge(d, x+20, y+16, name, color, tint, size=23, px=13, py=6)
        d.text((x+20, y+78), "职责", font=ft(22, True), fill=color)
        put(d, x+91, y+73, duty, 24, INK, True, card_w-110, 6)
        line(d, ((x+20, y+171), (x+card_w-20, y+171)), LINE, 1)
        d.text((x+20, y+195), "局限", font=ft(22, True), fill=MUTED)
        put(d, x+91, y+190, limit, 23, BODY, False, card_w-110, 6)

    # Relationships occupy the gutters, leaving each role card readable.
    put(d, 462, 477, "目标与授权\n执行与反馈", 22, MUTED, False, 156, 4, "center")
    arrow(d, (461, 545), (619, 545), BLUE_D, 3, 9)
    arrow(d, (619, 563), (461, 563), BLUE_D, 3, 9)

    arrow(d, (82, 681), (82, 907), BLUE_D, 3, 10)
    line(d, ((82, 790), (106, 790)), BLUE_D, 3)
    put(d, 112, 759, "人确认业务事实、\n契约和关键决策。", 22, MUTED, False, 280, 5)

    arrow(d, (998, 681), (998, 907), TEAL, 3, 10)
    line(d, ((974, 790), (998, 790)), TEAL, 3)
    put(d, 728, 759, "AI 按授权提交；\n人审核合并或回退。", 22, MUTED, False, 238, 5, "right")

    arrow(d, (617, 682), (466, 904), AMBER, 3, 10)
    rr(d, (438, 736, 642, 821), BG, AMBER, 14, 3)
    put(d, 447, 751, "AI 更新文档\n人确认关键约定", 22, MUTED, False, 186, 5, "center")

    put(d, 463, 1014, "文档记证据\nGit 追踪版本", 22, MUTED, False, 154, 4, "center")
    arrow(d, (461, 1083), (619, 1083), AMBER, 3, 9)
    arrow(d, (619, 1101), (461, 1101), AMBER, 3, 9)

    return im


def page5():
    im, d = header_footer(5, "让流程真正落地，还要补齐这几步",
                          "开工前选好方向；执行中留证据；出问题先归因再恢复。",
                          "看一个真实的小工具如何走完闭环")
    badge(d, 58, 211, "按推进时机，补齐容易漏掉的动作", BLUE_D, BLUE_L, size=21)
    def panel(top, bottom, stage, color, rows):
        rr(d, (58, top, 1022, bottom), PAPER, LINE, 18, 2)
        badge(d, 80, top+18, stage, color, {TEAL: TEAL_L, BLUE: BLUE_L, AMBER: AMBER_L}[color], 27)
        # Place content using measured text heights so the spare space is shared.
        body_offset = 43
        heights = []
        for _, title, body in rows:
            body_lines = wrapped(d, body, ft(22), 895)
            last_bottom = d.textbbox((0, 0), body_lines[-1], font=ft(22))[3]
            heights.append(body_offset + (len(body_lines)-1)*29 + last_bottom)
        y = top + (80 if len(rows) > 1 else 74)
        spacing = ((bottom-24-y-sum(heights))/(len(rows)-1)) if len(rows) > 1 else 0
        for (_, title, body), height in zip(rows, heights):
            d.text((88, y), title, font=ft(25, True), fill=INK)
            put(d, 88, y+body_offset, body, 22, MUTED, False, 895, 7)
            y += height + spacing

    panel(264, 588, "项目前 · 定方向和结构", TEAL, [
        (342, "方案与参考", "先对齐目标与验收；按需限时看 GitHub / 官方实现，查维护与许可。重大取舍可请多个 AI 独立挑错，由人决定。"),
        (466, "任务与目录", "按依赖、风险和不确定性拆任务，先跑通最小闭环。README 导航；按需用 AGENTS 指引 AI。分清源码、测试、输入副本、正式证据与临时产物。"),
    ])
    panel(604, 1080, "项目中 · 小步推进和归因", BLUE, [
        (681, "开工预检", "核对输入、隐私与凭据、权限、目标环境和回滚点；外部写入先获授权。插件或 MCP 按需使用。"),
        (807, "逐段推进", "工作副本中小步实现 → 自动验证 → 必要时人工确认 → 保存证据和 Git 检查点。"),
        (929, "异常归因", "先看受影响验收项、现象和严重度；沿需求、方案、输入、实现、依赖、环境、权限、验证与记录查证据。证据不足标待查；阻塞问题暂停相关依赖任务。"),
    ])
    panel(1096, 1286, "项目后 · 验收交接和运行", AMBER, [
        (1172, "交付复盘", "修复后重验；区分已构建、已发布、已可用。HANDOFF 写明未完成项、运行维护责任与恢复办法；分别评价规则遵循度和实际效用。"),
    ])
    return im


def page6():
    im, d = header_footer(6, "库存查询工具，怎样走完项目闭环？",
                          "闭环是在约定范围内有证据地完成，并能交接，而不是不断加功能。",
                          "通过不同项目的实践与验证，持续优化流程。", title_size=49)
    badge(d, 58, 263, "真实案例 · 从最小需求到可交接成果", BLUE_D, BLUE_L, size=21)
    stages = [
        (326, 474, "目标与边界", "快速查询不同地点的商品库存。首版只做关键词查询，使用虚构数据、本地运行。\n暂不做登录、云部署、CSV 和写操作。"),
        (496, 644, "需求与方案", "固定查询样例与预期结果；选择 SQLite + API + Vue。\n拆成任务 A（数据与接口）、任务 B（查询页面），先完成后端，再接前端。"),
        (666, 870, "实现与验证", "任务 A：21 项测试通过 → 人确认结果、批准继续 → 任务 B：累计 30 项测试通过。\n另做真实 HTTP、页面状态与不同屏幕布局检查；保存证据与 Git 检查点。"),
        (892, 1082, "交付与运行", "类型检查、测试和构建通过后，冻结归档、合并 main。交接记录（HANDOFF）写清运行方法、恢复点和未完成范围。\n本地可运行，不等于已部署或生产可用。"),
    ]
    for i, (top, bottom, title, body) in enumerate(stages):
        rr(d, (58, top, 1022, bottom), PAPER, FLOW_LINE, 18, 3)
        put(d, 82, top+14, title, 27, INK, True, 910, 4)
        put(d, 82, top+59, body, 22, BODY, False, 910, 7)
        if i < len(stages)-1:
            arrow(d, (540, bottom+2), (540, stages[i+1][0]-2), TEAL, 3, 8)
    rr(d, (58, 1104, 1022, 1214), AMBER_L, radius=18)
    put(d, 82, 1117, "遇到问题，先查证据再归因", 25, INK, True, 910, 4)
    put(d, 82, 1158, "类型检查遇到依赖兼容问题 → 核对版本 → 调整依赖 → 回归验证。", 22, BODY, False, 910, 5)
    arrow(d, (87, 1259), (121, 1259), TEAL, 3, 10)
    put(d, 138, 1238, "复盘与反馈：记录有效做法和不足，带入下一轮项目与方案。", 22, MUTED, False, 850, 5)
    return im


RENDERERS = [page1, page2, page3, page4, page5, page6]


def cover_samples():
    for variant in ("A", "B", "C"):
        im = page1()
        d = ImageDraw.Draw(im)
        d.rectangle((0, 107, W, 255), fill=BG)
        first, second = "AI 会写代码", "为什么项目还是卡住？"
        orange = "#D78942"
        if variant == "A":
            rr(d, (53, 204, 555, 238), "#DFE8FC", radius=10)
        put(d, 58, 131, first, 49, INK, True)
        put(d, 58, 184, second, 49, BLUE_D, True)
        key_x = 58 + tw(d, "为什么项目还是", ft(49, True))
        key_w = tw(d, "卡住", ft(49, True))
        if variant == "A":
            points = [(key_x+i, 243+3*math.sin(i/10)) for i in range(int(key_w)+1)]
            line(d, points, orange, 4)
        elif variant == "B":
            # A small tangled route: decoration stays inside the title area.
            line(d, ((742, 159), (779, 159), (812, 187), (779, 213), (751, 189), (784, 174), (820, 199)), BLUE, 4)
            arrow(d, (820, 199), (853, 169), orange, 4, 10)
            d.ellipse((736, 153, 748, 165), fill=orange)
        else:
            d.ellipse((key_x-8, 186, key_x+key_w+9, 249), outline=orange, width=3)
            badge(d, 711, 153, "代码之外的问题", BLUE_D, BLUE_L, 20)
        out = ROOT / f"cover-sample-{variant.lower()}.png"
        im.save(out, "PNG", optimize=True)
        print(out)


def cover_sample_a2():
    im = page1()
    d = ImageDraw.Draw(im)
    d.rectangle((0, 107, W, 255), fill=BG)
    x, title_y, title_size = 58, 131, 56
    key_x = 0
    for text, color in (("AI 会写代码，", "#111111"), ("为什么项目还是", BLUE_D), ("卡住", "#D64D54"), ("？", BLUE_D)):
        if text == "卡住":
            key_x = x
        put(d, x, title_y, text, title_size, color, True)
        x += tw(d, text, ft(title_size, True))
    for i in range(10):
        xx = key_x - 5 + i*12
        line(d, ((xx, 204), (xx+6, 210)), "#D78942", 2)
        line(d, ((xx, 210), (xx+6, 204)), "#D78942", 2)
    body = im.crop((0, 263, W, 1308))
    d.rectangle((0, 263, W, 1308), fill=BG)
    im.paste(body, (0, 218))
    out = ROOT / "cover-sample-a2.png"
    im.save(out, "PNG", optimize=True)
    print(out)
    return im


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", type=int, choices=range(1, 7), help="render one page and refresh contact sheet")
    parser.add_argument("--cover-samples", action="store_true", help="render three separate cover variants")
    parser.add_argument("--cover-a2", action="store_true", help="render the playful A variant separately")
    args = parser.parse_args()
    if args.cover_a2:
        cover_sample_a2()
        return
    if args.cover_samples:
        cover_samples()
        return
    indices = [args.only] if args.only else list(range(1, 7))
    for idx in indices:
        im = cover_sample_a2() if idx == 1 else RENDERERS[idx-1]()
        if idx in (2, 3, 4, 6):
            # A single-line heading releases one line of vertical space.
            # Move the subtitle and body together, keeping the footer fixed.
            body = im.crop((0, 263, W, 1308))
            ImageDraw.Draw(im).rectangle((0, 263, W, 1308), fill=BG)
            im.paste(body, (0, 213))
        out = ROOT / f"ai-project-loop-{idx:02d}.png"
        im.save(out, "PNG", optimize=True)
        print(f"{out} {im.width}x{im.height} {out.stat().st_size}")

    pages = [Image.open(ROOT / f"ai-project-loop-{idx:02d}.png").convert("RGB") for idx in range(1, 7)]
    tw, th, gap = 324, 432, 22
    sheet = Image.new("RGB", (tw*3+gap*4, th*2+gap*3), "#E5EAF3")
    for i, im in enumerate(pages):
        thumb = im.resize((tw, th), Image.Resampling.LANCZOS)
        x = gap + (i % 3) * (tw + gap)
        y = gap + (i // 3) * (th + gap)
        sheet.paste(thumb, (x, y))
    contact = ROOT / "contact-sheet.png"
    sheet.save(contact, "PNG", optimize=True)
    print(f"{contact} {sheet.width}x{sheet.height} {contact.stat().st_size}")


if __name__ == "__main__":
    main()
