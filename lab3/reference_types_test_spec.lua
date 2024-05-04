local busted = require("busted")
local assert = require("luassert")

describe("Reference Type Test", function()
    it("Should check if Lua variables are reference types", function()
        local tbl1 = { key = "value" }
        local tbl2 = tbl1

        assert.is_same(tbl1, tbl2)

        tbl2.key = "modified value"
        assert.is_same(tbl1.key, "modified value")
    end)
end)