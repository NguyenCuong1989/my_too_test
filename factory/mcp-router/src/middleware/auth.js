"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateToken = exports.authenticateJWT = void 0;
const express_1 = require("express");
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const logger_1 = __importDefault(require("../utils/logger"));
const JWT_SECRET = process.env.JWT_SECRET || 'super-secret-mcp-key';
const authenticateJWT = (req, res, next) => {
    const authHeader = req.headers.authorization;
    if (authHeader) {
        const token = authHeader.split(' ')[1];
        jsonwebtoken_1.default.verify(token, JWT_SECRET, (err, user) => {
            if (err) {
                logger_1.default.warn({ err }, 'Invalid JWT token attempt');
                return res.sendStatus(403);
            }
            req.user = user;
            next();
        });
    }
    else {
        logger_1.default.warn('Missing authorization header');
        res.sendStatus(401);
    }
};
exports.authenticateJWT = authenticateJWT;
const generateToken = (payload) => {
    return jsonwebtoken_1.default.sign(payload, JWT_SECRET, { expiresIn: '24h' });
};
exports.generateToken = generateToken;
//# sourceMappingURL=auth.js.map
